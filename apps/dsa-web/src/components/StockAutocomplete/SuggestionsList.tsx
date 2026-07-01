/**
 * Stock search suggestion list.
 */

import type { CSSProperties } from 'react';
import type { StockSuggestion } from '../../types/stockIndex';
import { useUiLanguage } from '../../contexts/UiLanguageContext';
import type { UiTextKey } from '../../i18n/uiText';
import { Badge } from '../common';
import { cn } from '../../utils/cn';

export interface SuggestionsListProps {
  /** Suggestion list */
  suggestions: StockSuggestion[];
  /** Highlighted index */
  highlightedIndex: number;
  /** Selection callback */
  onSelect: (suggestion: StockSuggestion) => void;
  /** Mouse hover callback */
  onMouseEnter: (index: number) => void;
  /** Custom style (for Portal fixed positioning) */
  style?: CSSProperties;
}

export function SuggestionsList({
  suggestions,
  highlightedIndex,
  onSelect,
  onMouseEnter,
  style,
}: SuggestionsListProps) {
  if (suggestions.length === 0) {
    return null;
  }

  return (
    <ul
      id="suggestions-list"
      className="z-[100] border-x border-b rounded-b-lg rounded-t-none max-h-60 overflow-auto"
      style={{
        ...style,
        backgroundColor: 'hsl(var(--card) / 0.85)',
        borderColor: 'var(--border-accent)',
        boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3), -4px 0 15px -3px rgba(0, 0, 0, 0.2), 4px 0 15px -3px rgba(0, 0, 0, 0.2)',
      }}
      role="listbox"
    >
      {suggestions.map((suggestion, index) => (
        <li
          key={suggestion.canonicalCode}
          role="option"
          aria-selected={index === highlightedIndex}
          className={cn(
            'px-4 py-1 cursor-pointer flex items-center justify-between',
            'hover:bg-[var(--autocomplete-hover-bg)]/25',
            index === highlightedIndex && 'bg-[var(--autocomplete-hover-bg)]/25',
          )}
          onClick={() => onSelect(suggestion)}
          onMouseEnter={() => onMouseEnter(index)}
        >
          <div className="flex items-center gap-3">
            <MarketBadge market={suggestion.market} />

            <div className="flex flex-col">
              <span className="text-sm font-medium text-primary-text">
                {suggestion.nameZh}
              </span>
              <span className="text-sm text-secondary-text">
                {suggestion.displayCode}
              </span>
            </div>
          </div>

          <MatchTypeBadge matchType={suggestion.matchType} />
        </li>
      ))}
    </ul>
  );
}

const MARKET_BADGE_STYLES = {
  CN: 'border-danger/25 bg-danger/10 text-danger',
  HK: 'border-success/25 bg-success/10 text-success',
  US: 'border-cyan/25 bg-cyan/10 text-cyan',
  JP: 'border-indigo-500/25 bg-indigo-500/10 text-indigo-500',
  KR: 'border-rose-500/25 bg-rose-500/10 text-rose-500',
  INDEX: 'border-purple/25 bg-purple/10 text-purple',
  ETF: 'border-warning/25 bg-warning/10 text-warning',
  BSE: 'border-orange-500/25 bg-orange-500/10 text-orange-500',
} as const;

const MARKET_LABEL_KEYS: Record<string, string> = {
  CN: 'home.searchMarket.cn',
  HK: 'home.searchMarket.hk',
  US: 'home.searchMarket.us',
  JP: 'home.searchMarket.jp',
  KR: 'home.searchMarket.kr',
  INDEX: 'home.searchMarket.index',
  ETF: 'home.searchMarket.etf',
  BSE: 'home.searchMarket.bse',
};

function MarketBadge({ market }: { market: string }) {
  const { t } = useUiLanguage();
  const style = MARKET_BADGE_STYLES[market as keyof typeof MARKET_BADGE_STYLES];
  const labelKey = MARKET_LABEL_KEYS[market];

  if (!style || !labelKey) {
    throw new Error(`Unsupported market in stock suggestion: ${market}`);
  }

  return (
    <Badge variant="default" size="sm" className={cn('min-w-[3rem] justify-center shadow-none', style)}>
      {t(labelKey as UiTextKey)}
    </Badge>
  );
}

const MATCH_TYPE_STYLES: Record<string, string> = {
  exact: 'border-cyan/25 bg-cyan/10 text-cyan',
  prefix: 'border-purple/25 bg-purple/10 text-purple',
  contains: 'border-warning/25 bg-warning/10 text-warning',
  fuzzy: 'border-border/55 bg-elevated/75 text-muted-text',
};

const MATCH_TYPE_LABEL_KEYS: Record<string, string> = {
  exact: 'home.searchMatch.exact',
  prefix: 'home.searchMatch.prefix',
  contains: 'home.searchMatch.contains',
  fuzzy: 'home.searchMatch.fuzzy',
};

function MatchTypeBadge({ matchType }: { matchType: string }) {
  const { t } = useUiLanguage();
  const style = MATCH_TYPE_STYLES[matchType] || MATCH_TYPE_STYLES.fuzzy;
  const labelKey = MATCH_TYPE_LABEL_KEYS[matchType] || MATCH_TYPE_LABEL_KEYS.fuzzy;

  return (
    <Badge variant="default" size="sm" className={cn('shrink-0 shadow-none', style)}>
      {t(labelKey as UiTextKey)}
    </Badge>
  );
}

export default SuggestionsList;
