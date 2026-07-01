import type {
  PortfolioCashDirection,
  PortfolioCorporateActionType,
  PortfolioFxRefreshResponse,
  PortfolioImportCommitResponse,
  PortfolioImportParseResponse,
  PortfolioPositionItem,
  PortfolioSide,
} from '../types/portfolio';
import type { UiLanguage } from '../i18n/uiText';
import { toDateInputValue } from './format';

export type FxRefreshFeedback = {
  tone: 'neutral' | 'success' | 'warning';
  text: string;
};

export type PortfolioAlertVariant = 'info' | 'success' | 'warning' | 'danger';

export function getTodayIso(): string {
  return toDateInputValue(new Date());
}

export function formatMoney(value: number | undefined | null, currency = 'CNY'): string {
  if (value == null || Number.isNaN(value)) return '--';
  return `${currency} ${Number(value).toLocaleString('zh-CN', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })}`;
}

export function formatPct(value: number | undefined | null): string {
  if (value == null || Number.isNaN(value)) return '--';
  return `${value.toFixed(2)}%`;
}

export function formatSignedPct(value: number | undefined | null): string {
  if (value == null || Number.isNaN(value)) return '--';
  const sign = value > 0 ? '+' : '';
  return `${sign}${value.toFixed(2)}%`;
}

export function hasPositionPrice(row: PortfolioPositionItem): boolean {
  return row.priceAvailable !== false && row.priceSource !== 'missing';
}

export function formatPositionPrice(row: PortfolioPositionItem): string {
  if (!hasPositionPrice(row)) return '--';
  return row.lastPrice.toFixed(4);
}

export function formatPositionMoney(value: number, row: PortfolioPositionItem): string {
  if (!hasPositionPrice(row)) return '--';
  return formatMoney(value, row.valuationCurrency);
}

export function getPositionPriceLabel(row: PortfolioPositionItem, language: UiLanguage = 'en'): string {
  if (!hasPositionPrice(row)) return language === 'en' ? 'No price' : '缺价';
  if (row.priceSource === 'realtime_quote') {
    return language === 'en'
      ? (row.priceProvider ? `Realtime · ${row.priceProvider}` : 'Realtime')
      : (row.priceProvider ? `实时价 · ${row.priceProvider}` : '实时价');
  }
  if (row.priceSource === 'history_close') {
    return language === 'en'
      ? (row.priceStale && row.priceDate ? `Close · ${row.priceDate}` : 'Close')
      : (row.priceStale && row.priceDate ? `收盘价 · ${row.priceDate}` : '收盘价');
  }
  return language === 'en' ? 'Unknown source' : '未知来源';
}

export function formatSideLabel(value: PortfolioSide, language: UiLanguage = 'en'): string {
  return value === 'buy' ? (language === 'en' ? 'Buy' : '买入') : (language === 'en' ? 'Sell' : '卖出');
}

export function formatCashDirectionLabel(value: PortfolioCashDirection, language: UiLanguage = 'en'): string {
  return value === 'in' ? (language === 'en' ? 'Inflow' : '流入') : (language === 'en' ? 'Outflow' : '流出');
}

export function formatCorporateActionLabel(value: PortfolioCorporateActionType, language: UiLanguage = 'en'): string {
  return value === 'cash_dividend' ? (language === 'en' ? 'Cash dividend' : '现金分红') : (language === 'en' ? 'Split adjustment' : '拆并股调整');
}

export function formatBrokerLabel(value: string, displayName?: string, language: UiLanguage = 'en'): string {
  if (displayName && displayName.trim()) return `${value}（${displayName.trim()}）`;
  const brokerNames: Record<string, Record<UiLanguage, string>> = {
    huatai: { zh: '华泰', en: 'Huatai' },
    citic: { zh: '中信', en: 'CITIC' },
    cmb: { zh: '招商', en: 'CMB' },
  };
  const name = brokerNames[value]?.[language];
  if (name) return `${value}（${name}）`;
  return value;
}

export function buildFxRefreshFeedback(data: PortfolioFxRefreshResponse, language: UiLanguage = 'en'): FxRefreshFeedback {
  if (data.refreshEnabled === false) {
    return {
      tone: 'neutral',
      text: language === 'en' ? 'Online FX refresh is disabled.' : '汇率在线刷新已被禁用。',
    };
  }

  if (data.pairCount === 0) {
    return {
      tone: 'neutral',
      text: language === 'en' ? 'No refreshable FX pairs in current scope.' : '当前范围无可刷新的汇率对。',
    };
  }

  if (data.updatedCount > 0 && data.staleCount === 0 && data.errorCount === 0) {
    return {
      tone: 'success',
      text: language === 'en'
        ? `FX refreshed, ${data.updatedCount} pair(s) updated.`
        : `汇率已刷新，共更新 ${data.updatedCount} 对。`,
    };
  }

  const summary = language === 'en'
    ? `Updated ${data.updatedCount}, still stale ${data.staleCount}, failed ${data.errorCount}.`
    : `更新 ${data.updatedCount} 对，仍过期 ${data.staleCount} 对，失败 ${data.errorCount} 对。`;
  if (data.staleCount > 0) {
    return {
      tone: 'warning',
      text: language === 'en'
        ? `Refresh attempted, but some pairs still use stale/fallback rates. ${summary}`
        : `已尝试刷新，但仍有部分货币对使用 stale/fallback 汇率。${summary}`,
    };
  }

  return {
    tone: 'warning',
    text: language === 'en'
      ? `Online refresh not fully successful. ${summary}`
      : `在线刷新未完全成功。${summary}`,
  };
}

export function getFxRefreshFeedbackVariant(tone: FxRefreshFeedback['tone']): PortfolioAlertVariant {
  if (tone === 'success') return 'success';
  if (tone === 'warning') return 'warning';
  return 'info';
}

export function getCsvParseVariant(result: PortfolioImportParseResponse): PortfolioAlertVariant {
  return result.errorCount > 0 || result.skippedCount > 0 ? 'warning' : 'info';
}

export function getCsvCommitVariant(result: PortfolioImportCommitResponse, isDryRun: boolean): PortfolioAlertVariant {
  if (isDryRun) return 'info';
  return result.failedCount > 0 || result.duplicateCount > 0 ? 'warning' : 'success';
}
