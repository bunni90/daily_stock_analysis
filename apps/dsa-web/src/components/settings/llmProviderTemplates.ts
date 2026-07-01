export type ChannelProtocol = 'openai' | 'deepseek' | 'gemini' | 'anthropic' | 'vertex_ai' | 'ollama';
export type LLMProviderCapability =
  | 'openai-compatible'
  | 'aggregator'
  | 'official-api'
  | 'model-discovery'
  | 'vision'
  | 'local-runtime';

export interface LLMProviderTemplate {
  channelId: string;
  label: string;
  protocol: ChannelProtocol;
  baseUrl: string;
  placeholderModels: string;
  capabilities: LLMProviderCapability[];
  configHint?: string;
  officialSources: Array<{
    label: string;
    url: string;
  }>;
}

import type { UiTextKey } from '../../i18n/uiText';

export type TranslateFn = (key: UiTextKey, params?: Record<string, string | number>) => string;

const CAPABILITY_I18N_KEYS: Record<LLMProviderCapability, { label: string; hint: string }> = {
  'openai-compatible': {
    label: 'settings.llm.template.capOpenaiCompatible',
    hint: 'settings.llm.template.capOpenaiCompatibleHint',
  },
  aggregator: {
    label: 'settings.llm.template.capAggregator',
    hint: 'settings.llm.template.capAggregatorHint',
  },
  'official-api': {
    label: 'settings.llm.template.capOfficialApi',
    hint: 'settings.llm.template.capOfficialApiHint',
  },
  'model-discovery': {
    label: 'settings.llm.template.capModelDiscovery',
    hint: 'settings.llm.template.capModelDiscoveryHint',
  },
  vision: {
    label: 'settings.llm.template.capVision',
    hint: 'settings.llm.template.capVisionHint',
  },
  'local-runtime': {
    label: 'settings.llm.template.capLocalRuntime',
    hint: 'settings.llm.template.capLocalRuntimeHint',
  },
};

export function getCapabilityLabels(t: TranslateFn): Record<LLMProviderCapability, { label: string; hint: string }> {
  const result: Record<string, { label: string; hint: string }> = {};
  for (const [cap, keys] of Object.entries(CAPABILITY_I18N_KEYS)) {
    result[cap] = { label: t(keys.label as UiTextKey), hint: t(keys.hint as UiTextKey) };
  }
  return result as Record<LLMProviderCapability, { label: string; hint: string }>;
}

export const LLM_PROVIDER_CAPABILITY_LABELS: Record<LLMProviderCapability, { label: string; hint: string }> = {
  'openai-compatible': {
    label: 'OpenAI 兼容',
    hint: '按 OpenAI-compatible endpoint 配置 Base URL，不额外拼接 /chat/completions。',
  },
  aggregator: {
    label: '聚合平台',
    hint: '模型可见性、路由和价格可能随账号权限与平台策略变化。',
  },
  'official-api': {
    label: '官方 API',
    hint: '使用服务商官方协议或官方兼容入口。',
  },
  'model-discovery': {
    label: '可获取模型',
    hint: '支持尝试通过 /models 获取模型列表；实际结果仍取决于账号权限和 API Key。',
  },
  vision: {
    label: 'Vision 提示',
    hint: '模板提示该 provider 常用于 Vision 场景；具体模型能力仍以账号和模型列表为准。',
  },
  'local-runtime': {
    label: '本地运行',
    hint: '需要当前运行环境能访问对应本地服务。',
  },
};

interface ProviderTemplateDef {
  channelId: string;
  labelKey: string;
  protocol: ChannelProtocol;
  baseUrl: string;
  placeholderModels: string;
  capabilities: LLMProviderCapability[];
  configHintKey?: string;
  officialSources: Array<{
    label: string;
    url: string;
  }>;
}

const PROVIDER_TEMPLATE_DEFS: ProviderTemplateDef[] = [
  {
    channelId: 'aihubmix',
    labelKey: 'settings.llm.template.provider.aihubmix',
    protocol: 'openai',
    baseUrl: 'https://aihubmix.com/v1',
    placeholderModels: 'gpt-5.5,claude-sonnet-4-6,gemini-3.1-pro-preview',
    capabilities: ['openai-compatible', 'aggregator'],
    officialSources: [{ label: 'AIHubmix', url: 'https://aihubmix.com/' }],
  },
  {
    channelId: 'anspire',
    labelKey: 'settings.llm.template.provider.anspire',
    protocol: 'openai',
    baseUrl: 'https://open-gateway.anspire.cn/v6',
    placeholderModels: 'Doubao-Seed-2.0-lite,Doubao-Seed-2.0-pro,qwen3.5-flash,MiniMax-M2.7',
    capabilities: ['openai-compatible'],
    configHintKey: 'settings.llm.template.provider.anspireHint',
    officialSources: [
      { label: 'Anspire Open', url: 'https://open.anspire.cn/?share_code=QFBC0FYC' },
      {
        label: 'LiteLLM OpenAI-compatible',
        url: 'https://docs.litellm.ai/docs/providers/openai_compatible',
      },
    ],
  },
  {
    channelId: 'deepseek',
    labelKey: 'settings.llm.template.provider.deepseek',
    protocol: 'deepseek',
    baseUrl: 'https://api.deepseek.com',
    placeholderModels: 'deepseek-v4-flash,deepseek-v4-pro',
    capabilities: ['official-api', 'openai-compatible'],
    officialSources: [{ label: 'DeepSeek API Docs', url: 'https://api-docs.deepseek.com/' }],
  },
  {
    channelId: 'dashscope',
    labelKey: 'settings.llm.template.provider.dashscope',
    protocol: 'openai',
    baseUrl: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    placeholderModels: 'qwen3.6-plus,qwen3.6-flash',
    capabilities: ['openai-compatible', 'model-discovery'],
    officialSources: [
      { label: 'DashScope Text Generation', url: 'https://help.aliyun.com/zh/model-studio/text-generation-model/' },
    ],
  },
  {
    channelId: 'zhipu',
    labelKey: 'settings.llm.template.provider.zhipu',
    protocol: 'openai',
    baseUrl: 'https://open.bigmodel.cn/api/paas/v4',
    placeholderModels: 'glm-5.1,glm-4.7-flash',
    capabilities: ['openai-compatible'],
    officialSources: [{ label: 'Zhipu Model Overview', url: 'https://docs.bigmodel.cn/cn/guide/start/model-overview' }],
  },
  {
    channelId: 'moonshot',
    labelKey: 'settings.llm.template.provider.moonshot',
    protocol: 'openai',
    baseUrl: 'https://api.moonshot.cn/v1',
    placeholderModels: 'kimi-k2.6,kimi-k2.5',
    capabilities: ['openai-compatible'],
    officialSources: [{ label: 'Kimi Platform Docs', url: 'https://platform.kimi.com/docs/models' }],
  },
  {
    channelId: 'minimax',
    labelKey: 'settings.llm.template.provider.minimax',
    protocol: 'openai',
    baseUrl: 'https://api.minimax.io/v1',
    placeholderModels: 'MiniMax-M3,MiniMax-M2.7,MiniMax-M2.7-highspeed',
    capabilities: ['openai-compatible'],
    officialSources: [
      { label: 'MiniMax OpenAI API', url: 'https://platform.minimax.io/docs/api-reference/text-chat' },
      { label: 'MiniMax Models', url: 'https://platform.minimax.io/docs/api-reference/models/openai/list-models' },
    ],
  },
  {
    channelId: 'volcengine',
    labelKey: 'settings.llm.template.provider.volcengine',
    protocol: 'openai',
    baseUrl: 'https://ark.cn-beijing.volces.com/api/v3',
    placeholderModels: 'doubao-seed-1-6-251015,doubao-seed-1-6-thinking-251015',
    capabilities: ['openai-compatible'],
    configHintKey: 'settings.llm.template.provider.volcengineHint',
    officialSources: [
      { label: 'Volcengine Ark Inference', url: 'https://www.volcengine.com/docs/82379/2121998' },
      { label: 'Volcengine Ark Models', url: 'https://www.volcengine.com/docs/82379/1949118' },
    ],
  },
  {
    channelId: 'siliconflow',
    labelKey: 'settings.llm.template.provider.siliconflow',
    protocol: 'openai',
    baseUrl: 'https://api.siliconflow.cn/v1',
    placeholderModels: 'deepseek-ai/DeepSeek-V3.2,Qwen/Qwen3-235B-A22B-Thinking-2507',
    capabilities: ['openai-compatible', 'model-discovery'],
    configHintKey: 'settings.llm.template.provider.siliconflowHint',
    officialSources: [{ label: 'SiliconFlow Models', url: 'https://docs.siliconflow.cn/quickstart/models' }],
  },
  {
    channelId: 'openrouter',
    labelKey: 'OpenRouter',
    protocol: 'openai',
    baseUrl: 'https://openrouter.ai/api/v1',
    placeholderModels: '~anthropic/claude-sonnet-latest,~openai/gpt-latest',
    capabilities: ['openai-compatible', 'aggregator', 'model-discovery'],
    configHintKey: 'settings.llm.template.provider.openrouterHint',
    officialSources: [
      { label: 'OpenRouter Models API', url: 'https://openrouter.ai/docs/api/api-reference/models/get-models' },
    ],
  },
  {
    channelId: 'gemini',
    labelKey: 'settings.llm.template.provider.gemini',
    protocol: 'gemini',
    baseUrl: '',
    placeholderModels: 'gemini-3.1-pro-preview,gemini-3-flash-preview',
    capabilities: ['official-api', 'vision'],
    officialSources: [{ label: 'Gemini Models', url: 'https://ai.google.dev/gemini-api/docs/models' }],
  },
  {
    channelId: 'anthropic',
    labelKey: 'settings.llm.template.provider.anthropic',
    protocol: 'anthropic',
    baseUrl: '',
    placeholderModels: 'claude-sonnet-4-6,claude-opus-4-7',
    capabilities: ['official-api'],
    officialSources: [
      { label: 'Anthropic Models', url: 'https://docs.anthropic.com/en/docs/about-claude/models/all-models' },
    ],
  },
  {
    channelId: 'openai',
    labelKey: 'settings.llm.template.provider.openai',
    protocol: 'openai',
    baseUrl: 'https://api.openai.com/v1',
    placeholderModels: 'gpt-5.5,gpt-5.4-mini',
    capabilities: ['official-api', 'openai-compatible', 'model-discovery'],
    officialSources: [{ label: 'OpenAI Models', url: 'https://platform.openai.com/docs/models' }],
  },
  {
    channelId: 'ollama',
    labelKey: 'settings.llm.template.provider.ollama',
    protocol: 'ollama',
    baseUrl: 'http://127.0.0.1:11434',
    placeholderModels: 'llama3.2,qwen2.5',
    capabilities: ['local-runtime'],
    configHintKey: 'settings.llm.template.provider.ollamaHint',
    officialSources: [{ label: 'Ollama API', url: 'https://github.com/ollama/ollama/blob/main/docs/api.md' }],
  },
  {
    channelId: 'custom',
    labelKey: 'settings.llm.template.provider.custom',
    protocol: 'openai',
    baseUrl: '',
    placeholderModels: 'model-name-1,model-name-2',
    capabilities: [],
    officialSources: [],
  },
];

function defToTemplate(def: ProviderTemplateDef, t: TranslateFn): LLMProviderTemplate {
  const isBrandNameOnly = !def.labelKey.startsWith('settings.llm.');
  return {
    channelId: def.channelId,
    label: isBrandNameOnly ? def.labelKey : t(def.labelKey as UiTextKey),
    protocol: def.protocol,
    baseUrl: def.baseUrl,
    placeholderModels: def.placeholderModels,
    capabilities: def.capabilities,
    configHint: def.configHintKey ? t(def.configHintKey as UiTextKey) : undefined,
    officialSources: def.officialSources,
  };
}

export function getProviderTemplates(t: TranslateFn): LLMProviderTemplate[] {
  return PROVIDER_TEMPLATE_DEFS.map((def) => defToTemplate(def, t));
}

export const LLM_PROVIDER_TEMPLATES: LLMProviderTemplate[] = PROVIDER_TEMPLATE_DEFS.map((def) => defToTemplate(def, (key) => key));

export const LLM_PROVIDER_TEMPLATE_BY_ID: Record<string, LLMProviderTemplate> = Object.fromEntries(
  LLM_PROVIDER_TEMPLATES.map((template) => [template.channelId, template]),
);

export function getProviderTemplateById(channelId: string, t: TranslateFn): LLMProviderTemplate | undefined {
  const def = PROVIDER_TEMPLATE_DEFS.find((d) => d.channelId === channelId);
  if (!def) {
    return undefined;
  }
  return defToTemplate(def, t);
}

export function getProviderTemplate(channelId: string): LLMProviderTemplate | undefined {
  if (!Object.prototype.hasOwnProperty.call(LLM_PROVIDER_TEMPLATE_BY_ID, channelId)) {
    return undefined;
  }
  return LLM_PROVIDER_TEMPLATE_BY_ID[channelId];
}

export function isKnownProviderTemplate(channelId: string): boolean {
  return channelId !== 'custom' && Boolean(getProviderTemplate(channelId));
}

export const MODEL_PLACEHOLDERS_BY_PROTOCOL: Record<ChannelProtocol, string> = {
  openai: 'gpt-5.5,qwen3.6-plus',
  deepseek: 'deepseek-v4-flash,deepseek-v4-pro',
  gemini: 'gemini-3.1-pro-preview,gemini-3-flash-preview',
  anthropic: 'claude-sonnet-4-6,claude-opus-4-7',
  vertex_ai: 'gemini-3.1-pro-preview',
  ollama: 'llama3.2,qwen2.5',
};
