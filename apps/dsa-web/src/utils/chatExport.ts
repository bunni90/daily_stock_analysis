import type { Message } from '../stores/agentChatStore';
import type { UiLanguage } from '../i18n/uiText';

export function formatSessionAsMarkdown(messages: Message[], language: UiLanguage = 'en'): string {
  const now = new Date();
  const locale = language === 'en' ? 'en-US' : 'zh-CN';
  const timeStr = now.toLocaleString(locale, {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  });

  const sessionTitle = language === 'en' ? 'Ask Session' : '问股会话';
  const generatedLabel = language === 'en' ? 'Generated at' : '生成时间';
  const userLabel = language === 'en' ? 'User' : '用户';

  const lines: string[] = [
    `# ${sessionTitle}`,
    '',
    `${generatedLabel}: ${timeStr}`,
    '',
  ];

  for (const msg of messages) {
    const heading = msg.role === 'user' ? `## ${userLabel}` : '## AI';
    if (msg.role === 'assistant' && msg.skillName) {
      lines.push(`${heading} (${msg.skillName})`);
    } else {
      lines.push(heading);
    }
    lines.push('');
    lines.push(msg.content);
    lines.push('');
  }

  return lines.join('\n');
}

export function downloadSession(messages: Message[], language: UiLanguage = 'en'): void {
  const content = formatSessionAsMarkdown(messages, language);
  const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
  const now = new Date();
  const dateStr = now.toISOString().slice(0, 10).replace(/-/g, '');
  const pad = (n: number) => n.toString().padStart(2, '0');
  const timeStr = pad(now.getHours()) + pad(now.getMinutes());
  const prefix = language === 'en' ? 'ask_session' : '问股会话';
  const filename = `${prefix}_${dateStr}_${timeStr}.md`;

  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
