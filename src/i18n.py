# -*- coding: utf-8 -*-
"""Backend i18n for API responses, error messages, and UI-facing strings.

Reads REPORT_LANGUAGE to select the language, defaults to zh.
"""

from __future__ import annotations

import os
from typing import Optional

from src.report_language import normalize_report_language

_MESSAGES: dict[str, dict[str, str]] = {}


def _m(key: str, zh: str, en: str, ko: str = "") -> None:
    _MESSAGES[key] = {"zh": zh, "en": en, "ko": ko or en}


def t(key: str, language: Optional[str] = None, **kwargs) -> str:
    lang = normalize_report_language(language or os.getenv("REPORT_LANGUAGE"))
    template = _MESSAGES.get(key, {}).get(lang) or _MESSAGES.get(key, {}).get("zh", key)
    if kwargs:
        try:
            return template.format(**kwargs)
        except (KeyError, IndexError):
            return template
    return template


def get_language() -> str:
    return normalize_report_language(os.getenv("REPORT_LANGUAGE"))


# --- API: error handler middleware ---
_m("api.internal_error", "服务器内部错误，请稍后重试", "Internal server error. Please try again later.")
_m("api.validation_error", "请求参数验证失败", "Request validation failed")
_m("api.internal_error_short", "服务器内部错误", "Internal server error")

# --- API: analysis endpoint ---
_m("analysis.market_review_no_report", "大盘复盘未返回可持久化报告", "Market review returned no persistable report")
_m("analysis.invalid_stock_input", "请输入有效的股票代码或股票名称", "Please enter a valid stock code or stock name")
_m("analysis.complete_sync", "分析完成（同步模式）", "Analysis complete (sync mode)")
_m("analysis.accepted_async", "分析任务已接受（异步模式）", "Analysis task accepted (async mode)")
_m("analysis.bad_request", "请求参数错误", "Bad request")
_m("analysis.duplicate_rejected", "股票正在分析中，拒绝重复提交", "Stock is already being analyzed; duplicate submission rejected")
_m("analysis.failed", "分析失败", "Analysis failed")
_m("analysis.need_stock_code", "必须提供 stock_code 或 stock_codes 参数", "stock_code or stock_codes parameter is required")
_m("analysis.batch_limit", "单次分析请求最多支持 {n} 只股票", "Maximum {n} stocks per analysis request")
_m("analysis.empty_stock_code", "股票代码不能为空或仅包含空白字符", "Stock code cannot be empty or whitespace")
_m("analysis.sync_single_only", "同步模式仅支持单只股票分析，请使用 async_mode=true 进行批量分析", "Sync mode only supports single stock analysis. Use async_mode=true for batch analysis")
_m("analysis.task_queued", "分析任务已加入队列: {code}", "Analysis task queued: {code}")
_m("analysis.batch_result", "已提交 {accepted} 个任务，{duplicates} 个重复跳过", "Submitted {accepted} tasks, {duplicates} duplicates skipped")
_m("analysis.stock_failed", "分析股票 {code} 失败", "Analysis failed for stock {code}")
_m("analysis.error_occurred", "分析过程发生错误: {error}", "Error during analysis: {error}")
_m("analysis.market_review_accepted", "大盘复盘任务已接受", "Market review task accepted")
_m("analysis.market_review_running", "大盘复盘正在执行", "Market review is running")
_m("analysis.market_review_submit_failed", "提交失败", "Submit failed")
_m("analysis.market_review_duplicate", "大盘复盘正在执行中，请稍后再试", "Market review is already running. Please try again later.")
_m("analysis.market_review_name", "大盘复盘", "Market Review")
_m("analysis.market_review_submitted", "大盘复盘任务已提交", "Market review task submitted")
_m("analysis.market_review_result", "大盘复盘任务已提交，完成后会保存报告并按配置推送通知", "Market review task submitted. Report will be saved and notifications sent upon completion.")
_m("analysis.task_list", "任务列表", "Task List")
_m("analysis.task_not_found", "任务不存在", "Task not found")
_m("analysis.task_expired", "任务 {id} 不存在或已过期", "Task {id} not found or expired")
_m("analysis.task_query_failed", "查询任务运行流失败: {error}", "Failed to query task flow: {error}")
_m("analysis.task_status_query_failed", "查询任务状态失败: {error}", "Failed to query task status: {error}")

# --- API: stocks endpoint ---
_m("stocks.empty_code", "股票代码不能为空", "Stock code cannot be empty")
_m("stocks.invalid_format", "'{code}' 不是合法的股票代码格式", "'{code}' is not a valid stock code format")
_m("stocks.extracted_codes", "提取的股票代码", "Extracted stock codes")
_m("stocks.no_file", "未提供文件，请使用表单字段 file 上传图片", "No file provided. Upload an image using form field 'file'")
_m("stocks.unsupported_type", "不支持的类型: {type}。允许: {allowed}", "Unsupported type: {type}. Allowed: {allowed}")
_m("stocks.image_too_large", "图片超过 {size}MB 限制", "Image exceeds {size}MB limit")
_m("stocks.read_upload_failed", "读取上传文件失败", "Failed to read uploaded file")
_m("stocks.extract_failed", "图片提取失败", "Image extraction failed")
_m("stocks.json_parse_failed", "JSON 解析失败: {error}", "JSON parse failed: {error}")
_m("stocks.no_text", "未提供 text，请使用 {\"text\": \"...\"}", "No text provided. Use {\"text\": \"...\"}")
_m("stocks.no_file_form", "未提供文件，请使用表单字段 file", "No file provided. Use form field 'file'")
_m("stocks.file_too_large", "文件超过 {size}MB 限制", "File exceeds {size}MB limit")
_m("stocks.read_file_failed", "读取文件失败", "Failed to read file")
_m("stocks.wrong_content_type", "请使用 multipart/form-data 上传文件，或 application/json 提交 {\"text\": \"...\"}", "Use multipart/form-data to upload a file, or application/json with {\"text\": \"...\"}")
_m("stocks.watchlist_count", "当前自选 {count} 只股票", "{count} stocks in watchlist")
_m("stocks.watchlist_failed", "获取自选队列失败: {error}", "Failed to get watchlist: {error}")
_m("stocks.added", "已加入 {code}", "Added {code}")
_m("stocks.add_failed", "加入自选失败: {error}", "Failed to add to watchlist: {error}")
_m("stocks.removed", "已移除 {code}", "Removed {code}")
_m("stocks.remove_failed", "从自选删除失败: {error}", "Failed to remove from watchlist: {error}")
_m("stocks.quote_not_found", "未找到股票 {code} 的行情数据", "Quote data not found for stock {code}")
_m("stocks.realtime_failed", "获取实时行情失败: {error}", "Failed to get real-time quote: {error}")
_m("stocks.history_failed", "获取历史行情失败: {error}", "Failed to get historical quotes: {error}")

# --- API: auth endpoint ---
_m("auth.password_already_exists", "已存在管理员密码，请启用认证后通过修改密码功能更新", "Admin password already exists. Enable auth and use change password to update.")
_m("auth.enter_password", "请输入要设置的管理员密码", "Please enter the admin password to set")
_m("auth.password_mismatch", "两次输入的密码不一致", "Passwords do not match")
_m("auth.set_password_first", "开启密码登录前请先设置密码", "Please set a password before enabling password login")
_m("auth.enter_current_password", "重新开启认证前请输入当前密码", "Please enter current password before re-enabling auth")
_m("auth.current_password_wrong", "当前密码错误", "Current password is incorrect")
_m("auth.enter_password_before_disable", "关闭认证前请输入当前密码", "Please enter current password before disabling auth")
_m("auth.enter_password_login", "请输入密码", "Please enter password")
_m("auth.wrong_password", "密码错误", "Incorrect password")
_m("auth.enter_current_to_change", "请输入当前密码", "Please enter current password")
_m("auth.new_password_mismatch", "两次输入的新密码不一致", "New passwords do not match")

# --- API: agent tool names ---
_m("tool.get_realtime_quote", "获取实时行情", "Get Real-time Quote")
_m("tool.get_historical_kline", "获取历史K线", "Get Historical K-line")
_m("tool.analyze_chip_distribution", "分析筹码分布", "Analyze Chip Distribution")
_m("tool.get_analysis_context", "获取分析上下文", "Get Analysis Context")
_m("tool.get_stock_fundamentals", "获取股票基本面", "Get Stock Fundamentals")
_m("tool.search_stock_news", "搜索股票新闻", "Search Stock News")
_m("tool.search_intelligence", "搜索综合情报", "Search Intelligence")
_m("tool.analyze_technical_trend", "分析技术趋势", "Analyze Technical Trend")
_m("tool.calculate_ma_system", "计算均线系统", "Calculate MA System")
_m("tool.analyze_volume_change", "分析量能变化", "Analyze Volume Change")
_m("tool.identify_kline_pattern", "识别K线形态", "Identify K-line Pattern")
_m("tool.get_market_indices", "获取市场指数", "Get Market Indices")
_m("tool.analyze_industry_sectors", "分析行业板块", "Analyze Industry Sectors")
_m("tool.get_skill_backtest_overview", "获取技能回测概览", "Get Skill Backtest Overview")
_m("tool.get_strategy_backtest_overview", "获取策略回测概览", "Get Strategy Backtest Overview")
_m("tool.get_stock_backtest_data", "获取个股回测数据", "Get Stock Backtest Data")

# --- API: portfolio endpoint ---
_m("portfolio.task_queued", "分析任务已加入队列: {code}", "Analysis task queued: {code}")

# --- API: app OpenAPI ---
_m("api.app_description", "A股/港股/美股自选股智能分析系统 API", "A-share / HK / US Stock Intelligent Analysis System API")
_m("api.feature_analysis", "- 股票分析：触发 AI 智能分析", "- Stock Analysis: Trigger AI-powered analysis")
_m("api.feature_history", "- 历史记录：查询历史分析报告", "- History: Query historical analysis reports")
_m("api.feature_data", "- 股票数据：获取行情数据", "- Stock Data: Get market data")
_m("api.health_check", "健康检查", "Health Check")
_m("api.health_check_desc", "用于负载均衡器或监控系统检查服务状态", "For load balancers or monitoring systems to check service status")

# --- API: analysis route summaries ---
_m("route.trigger_analysis", "触发股票分析", "Trigger Stock Analysis")
_m("route.trigger_analysis_desc", "启动 AI 智能分析任务，支持同步和异步模式。异步模式下相同股票代码不允许重复提交。", "Start an AI analysis task. Supports sync and async modes. Duplicate stock codes are rejected in async mode.")
_m("route.trigger_market_review", "触发大盘复盘", "Trigger Market Review")
_m("route.trigger_market_review_desc", "提交一个后台大盘复盘任务...", "Submit a background market review task...")
_m("route.get_tasks", "获取分析任务列表", "Get Analysis Task List")
_m("route.get_tasks_desc", "获取当前所有分析任务，可按状态筛选", "Get all current analysis tasks, filterable by status")
_m("route.filter_status_desc", "筛选状态：pending, processing, completed, failed, cancel_requested, cancelled（支持逗号分隔多个）", "Filter by status: pending, processing, completed, failed, cancel_requested, cancelled (comma-separated)")
_m("route.sse_stream", "SSE 事件流", "SSE Event Stream")
_m("route.task_sse", "任务状态 SSE 流", "Task Status SSE Stream")
_m("route.task_sse_desc", "通过 Server-Sent Events 实时推送任务状态变化", "Real-time task status updates via Server-Sent Events")
_m("route.task_flow_snapshot", "任务运行流快照", "Task Flow Snapshot")
_m("route.get_task_flow", "获取分析任务运行流", "Get Analysis Task Flow")
_m("route.get_task_flow_desc", "根据 task_id 查询任务数据流/信息流快照...", "Query task data/info flow snapshot by task_id...")
_m("route.query_task_status", "查询分析任务状态", "Query Analysis Task Status")
_m("route.query_task_status_desc", "根据 task_id 查询单个任务的状态", "Query single task status by task_id")
_m("route.extract_from_image", "从图片提取股票代码", "Extract Stock Codes from Image")
_m("route.extract_from_image_desc", "上传截图/图片，通过 Vision LLM 提取股票代码。支持 JPEG、PNG、WebP、GIF，最大 5MB。", "Upload a screenshot/image to extract stock codes via Vision LLM. Supports JPEG, PNG, WebP, GIF, max 5MB.")
_m("route.parse_csv", "解析 CSV/Excel/剪贴板", "Parse CSV/Excel/Clipboard")
_m("route.parse_csv_desc", "上传 CSV/Excel 文件或粘贴文本，自动解析股票代码。文件上限 2MB，文本上限 100KB。", "Upload CSV/Excel or paste text to auto-parse stock codes. File max 2MB, text max 100KB.")

# --- Services: task_service ---
_m("task_service.empty_code", "股票代码不能为空或仅包含空白字符", "Stock code cannot be empty or whitespace")
_m("task_service.submitted", "分析任务已提交，将异步执行并推送通知", "Analysis task submitted. Will execute asynchronously and send notifications.")
_m("task_service.empty_result", "分析返回空结果", "Analysis returned empty results")

# --- Services: import_parser ---
_m("import.file_too_large", "文件超过 {size}MB 限制", "File exceeds {size}MB limit")
_m("import.xlsx_hint", "请确认：(1) 文件为 .xlsx 格式；(2) 工作表不为空；(3) 文件未损坏。", "Please verify: (1) file is .xlsx format; (2) worksheet is not empty; (3) file is not corrupted.")
_m("import.xls_hint", "若为 .xls 格式，请另存为 .xlsx 后重试。", "If the file is .xls format, please save as .xlsx and retry.")
_m("import.excel_parse_failed", "Excel 解析失败: {error}。{hint}", "Excel parse failed: {error}. {hint}")
_m("import.xls_only", "仅支持 .xlsx 格式，请将 .xls 另存为 .xlsx 后重试", "Only .xlsx format is supported. Please save .xls as .xlsx and retry")
_m("import.encoding_failed", "无法识别文件编码，请使用 UTF-8 或 GBK", "Cannot detect file encoding. Please use UTF-8 or GBK")
_m("import.csv_parse_failed", "CSV 解析失败：请检查分隔符是否一致、列数是否匹配。", "CSV parse failed: please check delimiter consistency and column count.")
_m("import.csv_parse_hint", "常见原因：引号未闭合、某行列数与其他行不一致。原始错误: {error}", "Common causes: unclosed quotes, inconsistent column count. Original error: {error}")
_m("import.text_too_large", "文本超过 {size}KB 限制", "Text exceeds {size}KB limit")

# --- Market review ---
_m("market_review.root_title", "# 🎯 大盘复盘", "# 🎯 Market Review")
_m("market_review.push_title", "🎯 大盘复盘", "🎯 Market Review")
_m("market_review.cn_title", "# A股大盘复盘", "# A-Share Market Review")
_m("market_review.us_title", "# 美股大盘复盘", "# US Market Review")
_m("market_review.hk_title", "# 港股大盘复盘", "# HK Market Review")
_m("market_review.jp_title", "# 日股大盘复盘", "# Japan Market Review")
_m("market_review.kr_title", "# 韩股大盘复盘", "# Korea Market Review")
_m("market_review.separator", "> 以下为下一市场大盘复盘", "> Next market review")
_m("market_review.no_data", "大盘复盘未返回可持久化报告", "Market review returned no persistable report")
_m("market_review.holiday_skip", "🎯 大盘复盘\n\n今日相关市场休市，已跳过大盘复盘。", "🎯 Market Review\n\nThe relevant market is closed today. Market review skipped.")

# --- Agent skills ---
_m("skill.category.trend", "趋势", "Trend")
_m("skill.category.pattern", "形态", "Pattern")
_m("skill.category.reversal", "反转", "Reversal")
_m("skill.category.framework", "框架", "Framework")
_m("skill.type_suffix", "类技能", " skills")
_m("skill.rule_ref", "关联核心理念：第", "Related core concept: Rule ")
_m("skill.applicable_scenario", "适用场景", "Applicable scenario")

# --- Decision action labels ---
_m("action.buy", "买入", "Buy")
_m("action.add", "加仓", "Add Position")
_m("action.hold", "持有", "Hold")
_m("action.reduce", "减仓", "Reduce")
_m("action.sell", "卖出", "Sell")
_m("action.watch", "观望", "Watch")
_m("action.avoid", "回避", "Avoid")
_m("action.alert", "预警", "Alert")

# --- Bot: dispatcher ---
_m("bot.command_failed", "命令执行失败", "Command failed")
_m("bot.rate_limit", "请求过于频繁，请 {time} 秒后再试", "Too many requests. Please wait {time} seconds.")
_m("bot.unknown_command", "未知命令: {cmd}", "Unknown command: {cmd}")
_m("bot.available_commands_hint", "发送 `{prefix}help` 查看可用命令。", "Send `{prefix}help` for available commands.")
_m("bot.admin_required", "此命令需要管理员权限", "This command requires admin privileges")
_m("bot.usage_hint", "{error}\n用法: `{usage}`", "{error}\nUsage: `{usage}`")
_m("bot.greeting", "你好！我是股票分析助手。\n发送 `{prefix}help` 查看可用命令。", "Hello! I'm the Stock Analysis Assistant.\nSend `{prefix}help` for available commands.")
_m("bot.command_error", "命令执行失败: {error}", "Command failed: {error}")

# --- Bot: analyze command ---
_m("bot.analyze.desc", "分析指定股票", "Analyze a specified stock")
_m("bot.analyze.enter_code", "请输入股票代码", "Please enter a stock code")
_m("bot.analyze.invalid_code", "无效的股票代码: {code}（A股6位数字 / 港股HK+5位数字 / 美股1-5个字母）", "Invalid stock code: {code} (A-share: 6 digits / HK: HK+5 digits / US: 1-5 letters)")
_m("bot.analyze.stock_code", "• 股票代码: `{code}`", "• Stock code: `{code}`")
_m("bot.analyze.report_type", "• 报告类型: {type}", "• Report type: {type}")
_m("bot.analyze.will_notify", "分析完成后将自动推送结果。", "Results will be pushed automatically when analysis completes.")
_m("bot.analyze.submit_failed", "提交分析任务失败: {error}", "Failed to submit analysis: {error}")
_m("bot.analyze.failed", "分析失败: {error}", "Analysis failed: {error}")

# --- Bot: market command ---
_m("bot.market.desc", "大盘复盘分析", "Market review analysis")
_m("bot.market.running", "⚠️ 大盘复盘正在执行中，请稍后再试。", "⚠️ Market review is already running. Please try again later.")
_m("bot.market.start_failed", "大盘复盘启动失败，已释放运行锁；请稍后重试", "Market review failed to start. Lock released; please try again later")
_m("bot.market.started", "✅ **大盘复盘任务已启动**", "✅ **Market review task started**")
_m("bot.market.analyzing", "正在分析：", "Analyzing:")
_m("bot.market.index_performance", "• 主要指数表现", "• Major index performance")
_m("bot.market.sector_hotspots", "• 板块热点分析", "• Sector hotspot analysis")
_m("bot.market.sentiment", "• 市场情绪判断", "• Market sentiment")
_m("bot.market.outlook", "• 后市展望", "• Market outlook")
_m("bot.market.will_notify", "分析完成后将自动推送结果。", "Results will be pushed automatically when analysis completes.")
_m("bot.market.holiday_skip", "🎯 大盘复盘\n\n今日相关市场休市，已跳过大盘复盘。", "🎯 Market Review\n\nThe relevant market is closed today. Market review skipped.")

# --- Bot: batch command ---
_m("bot.batch.desc", "批量分析自选股", "Batch analyze watchlist stocks")
_m("bot.batch.empty", "自选股列表为空，请先配置 STOCK_LIST", "Watchlist is empty. Please configure STOCK_LIST first")
_m("bot.batch.invalid_count", "数量必须大于0", "Count must be greater than 0")
_m("bot.batch.invalid_number", "无效的数量: {count}", "Invalid count: {count}")
_m("bot.batch.started", "✅ **批量分析任务已启动**", "✅ **Batch analysis task started**")
_m("bot.batch.count", "• 分析数量: {count} 只", "• Analysis count: {count} stocks")
_m("bot.batch.list", "• 股票列表: {list}", "• Stock list: {list}")
_m("bot.batch.will_notify", "分析完成后将自动推送汇总报告。", "Summary report will be pushed when all analyses complete.")

# --- Bot: help command ---
_m("bot.help.desc", "显示帮助信息", "Show help information")
_m("bot.help.unknown_cmd", "未知命令: {cmd}", "Unknown command: {cmd}")
_m("bot.help.header", "📚 **股票分析助手 - 命令帮助**", "📚 **Stock Analysis Assistant - Help**")
_m("bot.help.available", "可用命令：", "Available commands:")
_m("bot.help.footer", "💡 输入 {prefix}help <命令名> 查看详细用法", "💡 Enter {prefix}help <command> for detailed usage")
_m("bot.help.examples", "**示例：**", "**Examples:**")
_m("bot.help.admin_warning", "⚠️ **需要管理员权限**", "⚠️ **Requires admin privileges**")

# --- Bot: status command ---
_m("bot.status.desc", "显示系统状态", "Show system status")
_m("bot.status.inherit_model", "继承主模型", "Inherit primary model")
_m("bot.status.header", "📊 **股票分析助手 - 系统状态**", "📊 **Stock Analysis Assistant - Status**")
_m("bot.status.time", "🕐 时间:", "🕐 Time:")
_m("bot.status.platform", "💻 平台:", "💻 Platform:")
_m("bot.status.watchlist_section", "**📈 自选股配置**", "**📈 Watchlist Configuration**")
_m("bot.status.stock_count", "• 股票数量: {count} 只", "• Stock count: {count}")
_m("bot.status.more_stocks", " ... 等 {count} 只", " ... and {count} more")
_m("bot.status.stock_list", "• 股票列表:", "• Stock list:")
_m("bot.status.ai_section", "**🤖 AI 分析服务**", "**🤖 AI Analysis Service**")
_m("bot.status.primary_model", "• 主模型: {model}", "• Primary model: {model}")
_m("bot.status.agent_model", "• Agent 模型: {model}", "• Agent model: {model}")
_m("bot.status.llm_channels", "• LLM 渠道: {channels}", "• LLM channels: {channels}")
_m("bot.status.not_configured", "未配置", "Not configured")
_m("bot.status.search_section", "**🔍 搜索服务**", "**🔍 Search Service**")
_m("bot.status.notify_section", "**📢 通知渠道**", "**📢 Notification Channels**")
_m("bot.status.ready", "✅ **系统就绪，可以开始分析！**", "✅ **System ready for analysis!**")
_m("bot.status.not_ready", "⚠️ **AI 服务未配置，分析功能不可用**", "⚠️ **AI service not configured. Analysis unavailable**")
_m("bot.status.configure_hint", "请配置 LITELLM_MODEL、LLM_CHANNELS、LITELLM_CONFIG 或任一 provider API Key", "Please configure LITELLM_MODEL, LLM_CHANNELS, LITELLM_CONFIG, or a provider API key")

# --- Bot: ask command ---
_m("bot.ask.desc", "使用 Agent 技能分析股票", "Analyze stock using Agent skills")
_m("bot.ask.enter_code", "请输入股票代码。用法: /ask <股票代码[,代码2,...]> [技能名称]", "Please enter a stock code. Usage: /ask <code[,code2,...]> [skill_name]")
_m("bot.ask.at_least_one", "请输入至少一个有效的股票代码", "Please enter at least one valid stock code")
_m("bot.ask.max_stocks", "一次最多分析 5 只股票", "Maximum 5 stocks per analysis")
_m("bot.ask.agent_disabled", "⚠️ Agent 模式未开启，无法使用问股功能。\n请在配置中设置 `AGENT_MODE=true`。", "⚠️ Agent mode is not enabled.\nPlease set `AGENT_MODE=true` in configuration.")
_m("bot.ask.failed", "⚠️ 分析失败: {error}", "⚠️ Analysis failed: {error}")
_m("bot.ask.error", "⚠️ 问股执行出错: {error}", "⚠️ Ask execution error: {error}")
_m("bot.ask.analysis_failed", "[分析失败] {error}", "[Analysis failed] {error}")
_m("bot.ask.unknown_error", "未知错误", "Unknown error")
_m("bot.ask.exec_error", "执行异常: {error}", "Execution error: {error}")
_m("bot.ask.timeout_detail", "分析超时（未在 150 秒内完成）", "Analysis timed out (not completed within 150 seconds)")
_m("bot.ask.timeout", "分析超时", "Analysis timed out")
_m("bot.ask.default_summary", "{code} 分析完成", "{code} analysis complete")
_m("bot.ask.truncated", "... (已截断，完整分析请单独查询)", "... (truncated. Query individually for full analysis)")
_m("bot.ask.label_name", "**名称**", "**Name**")
_m("bot.ask.label_conclusion", "**结论**:", "**Conclusion**:")
_m("bot.ask.label_confidence", "**置信度**:", "**Confidence**:")
_m("bot.ask.label_trend", "**趋势**:", "**Trend**:")
_m("bot.ask.label_summary", "**摘要**:", "**Summary**:")
_m("bot.ask.label_action", "**操作建议**:", "**Action**:")
_m("bot.ask.label_risk", "**风险提示**:", "**Risk**:")
_m("bot.ask.label_key_levels", "**关键点位**:", "**Key Levels**:")
_m("bot.ask.portfolio_section", "## 组合视角", "## Portfolio View")
_m("bot.ask.portfolio_risk_score", "- 组合风险分: {score}", "- Portfolio risk score: {score}")
_m("bot.ask.portfolio_concentration", "- 行业集中: {text}", "- Industry concentration: {text}")
_m("bot.ask.portfolio_correlation", "- 相关性风险: {text}", "- Correlation risk: {text}")
_m("bot.ask.portfolio_suggestion", "- 调仓建议: {text}", "- Rebalance suggestion: {text}")
_m("bot.ask.portfolio_position", "- 建议仓位: {text}", "- Suggested position: {text}")

# --- Bot: chat command ---
_m("bot.chat.desc", "与 AI 助手进行自由对话 (需开启 Agent 模式)", "Free chat with AI assistant (requires Agent mode)")
_m("bot.chat.enter_question", "请提供要询问的问题。", "Please provide a question.")
_m("bot.chat.agent_disabled", "⚠️ Agent 模式未开启，无法使用对话功能。\n请在配置中设置 `AGENT_MODE=true`。", "⚠️ Agent mode is not enabled.\nPlease set `AGENT_MODE=true` in configuration.")
_m("bot.chat.enter_question_usage", "⚠️ 请提供要询问的问题。\n用法: `/chat <问题>`\n示例: `/chat 帮我分析一下茅台最近的走势`", "⚠️ Please provide a question.\nUsage: `/chat <question>`\nExample: `/chat Help me analyze Moutai's recent trend`")
_m("bot.chat.failed", "⚠️ 对话失败: {error}", "⚠️ Chat failed: {error}")
_m("bot.chat.error", "⚠️ 对话执行出错: {error}", "⚠️ Chat execution error: {error}")

# --- Bot: research command ---
_m("bot.research.agent_disabled", "⚠️ Agent 模式未开启，无法使用深度研究功能。\n请在配置中设置 `AGENT_MODE=true`。", "⚠️ Agent mode is not enabled.\nPlease set `AGENT_MODE=true` in configuration.")
_m("bot.research.timeout", "⏳ 深度研究超时（{duration}s / {limit}s），请稍后重试或缩小研究范围。", "⏳ Research timed out ({duration}s / {limit}s). Please retry later or narrow the scope.")

# --- Bot: strategies command ---
_m("bot.strategies.desc", "查看可用交易策略", "View available trading strategies")
_m("bot.strategies.empty", "📋 暂无可用策略。请检查 strategies/ 目录。", "📋 No strategies available. Check the strategies/ directory.")
_m("bot.strategies.no_active", "📋 当前没有激活的策略。", "📋 No active strategies.")
_m("bot.strategies.header", "📋 **交易策略列表**", "📋 **Trading Strategies**")
_m("bot.strategies.custom_tag", " (自定义)", " (custom)")
_m("bot.strategies.summary", "共 {total} 个策略，已激活 {active} 个", "{total} strategies, {active} active")
_m("bot.strategies.footer", "💡 使用 `/ask <股票代码> <策略名>` 指定策略分析", "💡 Use `/ask <stock_code> <strategy>` to analyze with a specific strategy")
_m("bot.strategies.failed", "⚠️ 获取策略列表失败: {error}", "⚠️ Failed to get strategy list: {error}")
_m("bot.strategies.cat_trend", "📈 趋势类", "📈 Trend")
_m("bot.strategies.cat_pattern", "📊 形态类", "📊 Pattern")
_m("bot.strategies.cat_reversal", "🔄 反转类", "🔄 Reversal")
_m("bot.strategies.cat_framework", "🧩 框架类", "🧩 Framework")

# --- Bot: history command ---
_m("bot.history.desc", "查看 Agent 对话历史", "View Agent conversation history")
_m("bot.history.storage_unavailable", "⚠️ 存储模块不可用，无法查询对话历史。", "⚠️ Storage module unavailable. Cannot query conversation history.")
_m("bot.history.cleared", "✅ 已清除当前会话 ({count} 条消息)", "✅ Current session cleared ({count} messages)")
_m("bot.history.clear_failed", "⚠️ 清除失败: {error}", "⚠️ Clear failed: {error}")
_m("bot.history.auth_check", "⚠️ 你只能查看自己的会话记录。", "⚠️ You can only view your own session history.")
_m("bot.history.no_messages", "📭 会话 `{id}` 无消息记录", "📭 Session `{id}` has no messages")
_m("bot.history.session_detail", "💬 **会话详情**: `{id}`", "💬 **Session details**: `{id}`")
_m("bot.history.get_detail_failed", "⚠️ 获取会话详情失败: {error}", "⚠️ Failed to get session details: {error}")
_m("bot.history.no_history", "📭 暂无对话历史记录", "📭 No conversation history")
_m("bot.history.header", "📋 **最近对话会话**", "📋 **Recent Sessions**")
_m("bot.history.new_conversation", "新对话", "New conversation")
_m("bot.history.msg_count", "   💬 {count} 条消息", "   💬 {count} messages")
_m("bot.history.footer", "💡 使用 `/history <session_id>` 查看具体会话内容", "💡 Use `/history <session_id>` to view session details")
_m("bot.history.get_list_failed", "⚠️ 获取会话列表失败: {error}", "⚠️ Failed to get session list: {error}")

# --- Run flow: data type labels ---
_m("runflow.dataType.realtime_quote", "实时行情", "Real-time Quote")
_m("runflow.dataType.daily_data", "日线K线", "Daily K-line")
_m("runflow.dataType.daily_bars", "日线K线", "Daily K-line")
_m("runflow.dataType.technical", "技术指标", "Technical Indicators")
_m("runflow.dataType.news", "新闻舆情", "News & Sentiment")
_m("runflow.dataType.news_search", "新闻舆情", "News & Sentiment")
_m("runflow.dataType.fundamental", "基本面", "Fundamentals")
_m("runflow.dataType.fundamentals", "基本面", "Fundamentals")
_m("runflow.dataType.belong_boards", "所属板块", "Belonging Sectors")
_m("runflow.dataType.chip", "筹码结构", "Chip Structure")

# --- Run flow: history runs ---
_m("runflow.history.saved", "报告历史已保存", "Report history saved")
_m("runflow.history.failed", "报告历史保存失败：{error}", "Report history save failed: {error}")
_m("runflow.history.saveLabel", "保存报告", "Save Report")
_m("runflow.history.saveEdge", "保存", "Save")
_m("runflow.history.successTitle", "历史保存成功", "History save succeeded")
_m("runflow.history.failedTitle", "历史保存失败", "History save failed")

# --- Run flow: notification runs ---
_m("runflow.notification.pushLabel", "推送通知 · {channel}", "Push Notification · {channel}")
_m("runflow.notification.edgeLabel", "通知", "Notify")
_m("runflow.notification.successTitle", "通知发送成功", "Notification sent successfully")
_m("runflow.notification.skippedTitle", "通知跳过", "Notification skipped")
_m("runflow.notification.failedTitle", "通知失败", "Notification failed")

# --- Run flow: LLM runs ---
_m("runflow.llm.successWithSwitch", "LLM {model} 成功，期间发生模型切换", "LLM {model} succeeded with model switch")
_m("runflow.llm.success", "LLM {model} 成功", "LLM {model} succeeded")
_m("runflow.llm.failed", "LLM {model} 失败：{error}", "LLM {model} failed: {error}")

# --- Run flow: notification run message ---
_m("runflow.notificationRun.success", "{channel} 通知发送成功", "{channel} notification sent successfully")
_m("runflow.notificationRun.skipped", "{channel} 通知跳过", "{channel} notification skipped")
_m("runflow.notificationRun.failed", "{channel} 通知失败：{error}", "{channel} notification failed: {error}")
_m("runflow.notificationRun.unknown", "{channel} 通知结果未知", "{channel} notification result unknown")

# --- Run flow: provider runs ---
_m("runflow.provider.started", "{label} 调用中", "{label} calling")
_m("runflow.provider.startedTitle", "{label}开始", "{label} started")
_m("runflow.provider.success", "{label} {provider} 成功", "{label} {provider} succeeded")
_m("runflow.provider.failed", "{label} {provider} 失败：{message}", "{label} {provider} failed: {message}")
_m("runflow.provider.successTitle", "{label}成功", "{label} succeeded")
_m("runflow.provider.failedTitle", "{label}失败", "{label} failed")
_m("runflow.provider.edgeLabel", "{label} · {provider}", "{label} · {provider}")

# --- Run flow: LLM runs ---
_m("runflow.llm.started", "LLM {model} 调用中", "LLM {model} calling")
_m("runflow.llm.startedTitle", "LLM 开始", "LLM started")
_m("runflow.llm.edgeLabel", "LLM 生成", "LLM Generation")
_m("runflow.llm.successTitle", "LLM 成功", "LLM succeeded")
_m("runflow.llm.failedTitle", "LLM 失败", "LLM failed")

# --- Run flow: data type labels (additional) ---
_m("runflow.dataType.history_save", "历史保存", "History Save")

# --- Run flow: summary status ---
_m("runflow.summary.normal", "正常", "Normal")
_m("runflow.summary.degraded", "部分降级", "Partially degraded")
_m("runflow.summary.failed", "失败", "Failed")
_m("runflow.summary.unknown", "未知", "Unknown")

# --- Run flow: analysis input status ---
_m("runflow.inputStatus.missing", "未进入本次分析输入", "Not included in analysis input")
_m("runflow.inputStatus.partial", "本次分析输入仅部分可用", "Analysis input only partially available")
_m("runflow.inputStatus.fallback", "本次分析输入使用降级数据", "Analysis input using fallback data")
_m("runflow.inputStatus.stale", "本次分析输入使用过期数据", "Analysis input using stale data")
_m("runflow.inputStatus.estimated", "本次分析输入使用估算数据", "Analysis input using estimated data")
_m("runflow.inputStatus.fetch_failed", "输入块显示抓取失败", "Input block fetch failed")
_m("runflow.inputStatus.not_supported", "输入块标记为不支持", "Input block marked as not supported")
_m("runflow.inputStatus.unknown", "输入块状态为 {status}", "Input block status is {status}")

# --- Run flow: diagnostic labels ---
_m("diagnostics.label.newsSearch", "新闻搜索", "News Search")
_m("diagnostics.label.llm", "LLM", "LLM")
_m("diagnostics.label.notification", "通知", "Notification")
_m("diagnostics.label.history", "历史保存", "History Save")
_m("diagnostics.label.realtimeQuote", "实时行情", "Real-time Quote")
_m("diagnostics.label.dailyData", "日线K线", "Daily K-line")

# --- Run flow: diagnostic messages ---
_m("diagnostics.news.noResults", "新闻搜索无结果", "News search returned no results")
_m("diagnostics.news.noDiagnosticInfo", "新闻搜索未记录诊断信息", "News search diagnostic info not recorded")
_m("diagnostics.news.noRawEvidence", "新闻检索未记录原始证据，可能未尝试或未启用", "News retrieval no raw evidence recorded, may not have been attempted or enabled")
_m("diagnostics.news.resultsOk", "新闻检索返回 {count} 条结果", "News retrieval returned {count} results")
_m("diagnostics.news.resultsButInputIssue", "新闻检索返回 {count} 条结果，但新闻{inputMessage}；报告页相关资讯可能来自后续检索或历史持久化", "News retrieval returned {count} results, but news {inputMessage}; report page news may come from subsequent retrieval or history")
_m("diagnostics.news.inputOnlyMessage", "新闻{inputMessage}；报告页相关资讯可能来自后续检索或历史持久化", "News {inputMessage}; report page news may come from subsequent retrieval or history")
_m("diagnostics.provider.noDiagnosticInfo", "{label}未记录诊断信息", "{label} diagnostic info not recorded")
_m("diagnostics.provider.successButInputIssue", "{label}{provider} 成功，但{inputMessage}", "{label} {provider} succeeded, but {inputMessage}")
_m("diagnostics.provider.successWithFallback", "{label}{provider} 成功，前置数据源失败后已继续", "{label} {provider} succeeded after prior data source failure")
_m("diagnostics.provider.success", "{label}{provider} 成功", "{label} {provider} succeeded")
_m("diagnostics.provider.failed", "{label}失败：{message}", "{label} failed: {message}")
_m("diagnostics.provider.allFailed", "所有数据源尝试失败", "All data source attempts failed")
_m("diagnostics.llm.success", "LLM {model} 成功", "LLM {model} succeeded")
_m("diagnostics.llm.successWithIssues", "LLM {model} 成功，期间发生过失败或模型切换", "LLM {model} succeeded with failures or model switches")
_m("diagnostics.llm.failed", "LLM 失败：{error}", "LLM failed: {error}")
_m("diagnostics.llm.successNoModel", "LLM 成功，模型未记录", "LLM succeeded, model not recorded")
_m("diagnostics.llm.noDiagnosticInfo", "LLM 未记录诊断信息", "LLM diagnostic info not recorded")
_m("diagnostics.notification.noDiagnosticInfo", "通知结果未记录", "Notification result not recorded")
_m("diagnostics.notification.partialFailure", "部分通知渠道失败，其余渠道已发送", "Some notification channels failed, others sent")
_m("diagnostics.notification.success", "通知发送成功", "Notification sent successfully")
_m("diagnostics.notification.notConfiguredOrSkipped", "通知未配置或本次跳过", "Notification not configured or skipped")
_m("diagnostics.notification.failed", "通知失败：{error}", "Notification failed: {error}")
_m("diagnostics.history.saved", "报告历史已保存", "Report history saved")
_m("diagnostics.history.failed", "报告历史保存失败：{error}", "Report history save failed: {error}")
_m("diagnostics.history.failedNoDetail", "报告历史保存失败", "Report history save failed")
_m("diagnostics.history.noDiagnosticInfo", "历史保存未记录诊断信息", "History save diagnostic info not recorded")
_m("diagnostics.summary.unknownReason", "旧报告或诊断证据不足，无法判断本次运行状态", "Legacy report or insufficient diagnostic evidence; unable to determine run status")

# --- Run flow: lane labels ---
_m("runflow.lane.entry", "入口", "Entry")
_m("runflow.lane.dataSource", "数据来源", "Data Source")
_m("runflow.lane.analysis", "分析引擎", "Analysis Engine")
_m("runflow.lane.artifact", "产物", "Artifact")

# --- Run flow: node labels ---
_m("runflow.node.userRequest", "用户请求", "User Request")
_m("runflow.node.taskQueue", "任务队列", "Task Queue")
_m("runflow.node.analysisPipeline", "分析流程", "Analysis Pipeline")
_m("runflow.node.saveReport", "保存报告", "Save Report")
_m("runflow.node.pushNotification", "推送通知", "Push Notification")
_m("runflow.node.llmGeneration", "LLM 生成", "LLM Generation")

# --- Run flow: edge labels ---
_m("runflow.edge.submit", "提交", "Submit")
_m("runflow.edge.schedule", "调度", "Schedule")
_m("runflow.edge.input", "输入", "Input")
_m("runflow.edge.generate", "生成", "Generate")
_m("runflow.edge.save", "保存", "Save")
_m("runflow.edge.notify", "通知", "Notify")
_m("runflow.edge.degrade", "降级", "Fallback")
_m("runflow.edge.retry", "重试", "Retry")
_m("runflow.edge.call", "调用", "Call")
_m("runflow.edge.assemble", "组装", "Assemble")

# --- Run flow: status labels ---
_m("runflow.status.success", "成功", "Succeeded")
_m("runflow.status.failed", "失败", "Failed")
_m("runflow.status.unknownError", "未知错误", "Unknown error")
_m("runflow.label.status", "状态", " Status")

# --- Run flow: messages ---
_m("runflow.message.taskRequestCreated", "任务请求已创建", "Task request created")
_m("runflow.message.historyRecord", "历史分析记录", "Historical analysis record")
_m("runflow.message.taskCompletedHistory", "任务已完成并进入历史记录", "Task completed and archived")
_m("runflow.message.historyRecordGenerated", "历史记录已生成", "History record generated")
_m("runflow.message.historyAlreadyExists", "历史记录已存在", "History record already exists")
_m("runflow.message.llmNoDiagnostic", "LLM 未记录诊断信息", "LLM diagnostic info not recorded")
_m("runflow.message.notificationNotRecorded", "通知结果未记录", "Notification result not recorded")
_m("runflow.message.noContextPackDiagnostic", "尚未记录输入上下文诊断", "Context pack diagnostic not recorded yet")
_m("runflow.message.noLlmDiagnostic", "尚未记录 LLM 诊断", "LLM diagnostic not recorded yet")
_m("runflow.message.noHistorySaveDiagnostic", "尚未记录历史保存结果", "History save result not recorded yet")
_m("runflow.message.noNotificationDiagnostic", "尚未记录通知结果", "Notification result not recorded yet")
_m("runflow.message.noContextPackOverview", "未记录 AnalysisContextPack overview", "AnalysisContextPack overview not recorded")
_m("runflow.message.contextPackAssembledWithCount", "输入上下文已组装，可用块 {available}", "Context pack assembled, {available} blocks available")
_m("runflow.message.contextPackAssembled", "输入上下文已组装", "Context pack assembled")
_m("runflow.message.taskQueued", "任务已加入队列", "Task queued")
_m("runflow.message.taskRunning", "任务执行中", "Task running")
_m("runflow.message.analysisComplete", "分析完成", "Analysis complete")

# --- Run flow: events ---
_m("runflow.event.taskCreated", "任务已创建", "Task created")
_m("runflow.event.taskStarted", "任务开始执行", "Task started")
_m("runflow.event.taskFailed", "任务失败", "Task failed")
_m("runflow.event.taskCancelled", "任务取消", "Task cancelled")
_m("runflow.event.taskCancelRequested", "任务请求取消", "Task cancel requested")
_m("runflow.event.taskCompleted", "任务完成", "Task completed")
_m("runflow.event.runEvent", "运行事件", "Run event")

# --- Run flow: context block messages ---
_m("runflow.contextBlock.available", "已进入本次分析输入", "Included in analysis input")
_m("runflow.contextBlock.fallback", "本次分析输入使用降级数据", "Analysis input using fallback data")
_m("runflow.contextBlock.partial", "本次分析输入仅部分可用", "Analysis input only partially available")
_m("runflow.contextBlock.stale", "本次分析输入使用过期数据", "Analysis input using stale data")
_m("runflow.contextBlock.estimated", "本次分析输入使用估算数据", "Analysis input using estimated data")
_m("runflow.contextBlock.fetch_failed", "输入块抓取失败", "Input block fetch failed")
_m("runflow.contextBlock.missingWithReason", "未进入本次分析输入：{reason}", "Not included in analysis input: {reason}")
_m("runflow.contextBlock.missing", "未进入本次分析输入", "Not included in analysis input")
_m("runflow.contextBlock.not_supported", "当前市场或链路不支持该输入块", "Input block not supported for current market or pipeline")
_m("runflow.contextBlock.unknown", "输入块状态为 {status}", "Input block status is {status}")

# --- Run flow: provider run messages ---
_m("runflow.providerRun.successWithCount", "{label} {provider} 成功，返回 {count} 条", "{label} {provider} succeeded, {count} records returned")
_m("runflow.providerRun.success", "{label} {provider} 成功", "{label} {provider} succeeded")
_m("runflow.providerRun.failed", "{label} {provider} 失败：{error}", "{label} {provider} failed: {error}")

# --- Run flow: task status messages ---
_m("runflow.taskStatus.queued", "任务已加入队列", "Task queued")
_m("runflow.taskStatus.running", "任务执行中", "Task running")
_m("runflow.taskStatus.completed", "任务已完成", "Task completed")
_m("runflow.taskStatus.failed", "任务失败", "Task failed")
_m("runflow.taskStatus.cancelRequested", "任务请求取消", "Task cancel requested")
_m("runflow.taskStatus.cancelled", "任务已取消", "Task cancelled")
_m("runflow.taskStatus.unknown", "任务状态未知", "Task status unknown")
