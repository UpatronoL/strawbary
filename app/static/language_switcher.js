document.addEventListener('DOMContentLoaded', () => {

  /**
   * 🍓 Translation Data Object
   * Contains all translations organized by language code (en, ja).
   */
  const translations = {
    en: {
      // Base template translations
      title: 'Strawberry Sensor',
      'nav-home': 'Home',
      'nav-measurements': 'Measurements',
      'nav-summary': 'Summary',
      'nav-analysis': 'Analysis',
      'nav-alert-history': 'Alert History',
      footer: 'Footer content',

      // Home page translations
      'dashboard-title': 'Strawberry Monitoring Dashboard',
      'dashboard-subtitle': 'Real-time environmental monitoring and analytics',
      'current-conditions': 'Current Environmental Conditions',
      'last-updated': 'Last updated:',
      'air-temperature': 'Air Temperature',
      'air-humidity': 'Air Humidity',
      'soil-moisture': 'Soil Moisture',
      'light-intensity': 'Light Intensity',
      'ground-temp': 'Ground Temp',
      'active-alerts': 'Active Alerts',
      'no-alerts': 'No active alerts. All systems operating normally.',
      'recent-alert-history': 'Recent Alert History',
      'view-full-history': 'View Full History',
      'todays-summary': "Today's Summary",
      'min-air-temp': 'Min Air Temp',
      'max-air-temp': 'Max Air Temp',
      'min-humidity': 'Min Humidity',
      'max-humidity': 'Max Humidity',
      'min-light': 'Min Light',
      'max-light': 'Max Light',
      'min-ground-temp': 'Min Ground Temp',
      'max-ground-temp': 'Max Ground Temp',
      'min-soil-moisture': 'Min Soil Moisture',
      'max-soil-moisture': 'Max Soil Moisture',
      'show-more': 'Show More',
      'show-less': 'Show Less',
      'readings-collected': 'readings collected today',
      'alert-analytics': 'Alert Analytics',
      'most-common-issue': 'Most Common Issue',
      'critical-alerts-24h': 'Critical Alerts (24h)',
      'system-reliability': 'System Reliability',
      'response-time': 'Response Time',
      'quick-actions': 'Quick Actions',
      'view-detailed-data': 'View Detailed Data',
      'analytics-dashboard': 'Analytics Dashboard',
      'download-report': 'Download Report',
      'refresh-now': 'Refresh Now',
      'smart-tip': 'Smart Tip',
      'system-online': 'All Systems Operational',
      'system-offline': 'System Offline - No Recent Data',
      'attention-required': 'Active Alerts - Attention Required',
      'alerts-24h': 'Alerts (24h)',
      'active-alerts-count': 'Active Alerts',
      'resolved-24h': 'Resolved (24h)',
      'avg-resolution': 'Avg Resolution',
      'data-fresh': 'Data is fresh',
      'data-stale': 'Data is stale',
      'next-refresh': 'Next refresh in:',
      'sensor-data-updates': 'Sensor data updates automatically every 5 minutes',

      // Table page translations
      'measurementsFor': 'Measurements for',
      'todayMeasurements': "Today's Measurements",
      'selectDate': 'Select Date:',
      apply: 'Apply',
      'showToday': 'Show Today',
      filterByDate: 'Filter by date:',
      showAll: 'Show All',
      filterValuePlaceholder: 'Filter Value',
      headerDate: 'Date',
      headerTime: 'Time',
      headerTemperature: 'Temperature (°C)',
      'headerSoilTemperature': 'Soil Temp', // NEW
      headerHumidity: 'Humidity (%)',
      headerGroundTemperature: 'Ground Temperature (°C)',
      'headerSoilHumidity': 'Soil Humidity', // NEW
      headerLightIntensity: 'Light Intensity (Lux)',
      downloadTitle: 'Export Data',
      downloadBtn: 'Download CSV',
      quickStats: 'Quick Stats',
      totalRecords: 'Total Records:',
      timeRange: 'Time Range:',
      searchPlaceholder: 'Search all columns...',
      lengthMenu: 'Show _MENU_ entries',
      info: 'Showing _START_ to _END_ of _TOTAL_ entries',
      
      // Summary page translations
      category: 'Category',
      metric: 'Metric',
      categories: {
        temperature: 'Temperature (°C)',
        humidity: 'Humidity (%)',
        light: 'Light Intensity',
        groundTemp: 'Ground Temperature (°C)',
        groundHumidity: 'Ground Humidity (%)'
      },
      metrics: {
        max: 'Max',
        min: 'Min',
        dailyAvg: 'Daily Avg',
        daytimeAvg: 'Daytime Avg',
        nighttimeAvg: 'Nighttime Avg'
      },

      // Analysis page translations
      'analysis-daily-title': "Today's Environmental Data Analysis",
      'analysis-weekly-title': 'Weekly Environmental Data Analysis',
      'analysis-temp': 'Temperature Patterns',
      'analysis-humidity': 'Humidity Patterns',
      'analysis-light': 'Light Intensity Patterns',
      'analysis-day-avg-temp': 'Daytime Temperature',
      'analysis-day-avg-humidity': 'Daytime Humidity',
      'analysis-day-avg-light': 'Daytime Light Intensity',
      'analysis-night-avg-temp': 'Nighttime Temperature',
      'analysis-night-avg-humidity': 'Nighttime Humidity',
      'analysis-night-avg-light': 'Nighttime Light Intensity',
      'analysis-whole-avg-temp': '24-Hour Temperature',
      'analysis-whole-avg-humidity': '24-Hour Humidity',
      'analysis-whole-avg-light': '24-Hour Light Intensity',
      
      // Analysis Chart Titles (NEW)
      'Temperature Analysis': 'Temperature Analysis',
      'Soil Temperature Analysis': 'Soil Temperature Analysis',
      'Humidity Analysis': 'Humidity Analysis',
      'Soil Humidity Analysis': 'Soil Humidity Analysis',
      'Light Intensity Analysis': 'Light Intensity Analysis',
      'Hourly (Today)': 'Hourly (Today)',
      'Daytime Avg (Weekly)': 'Daytime Avg (Weekly)',
      'Nighttime Avg (Weekly)': 'Nighttime Avg (Weekly)',
      '24-Hour Avg (Weekly)': '24-Hour Avg (Weekly)',
      
      // Alert History page translations
      'alert-history-title': 'Alert History',
      'alert-history-subtitle': 'Comprehensive alert tracking and analysis',
      'total-24h': 'Total (24h)',
      'resolved-24h-label': 'Resolved (24h)',
      'avg-resolution-label': 'Avg Resolution',
      'alert-type': 'Alert Type',
      'all-types': 'All Types',
      'alert-category': 'Category',
      'all-categories': 'All Categories',
      'alert-severity': 'Severity',
      'all-severities': 'All Severities',
      'alert-status': 'Status',
      'all-statuses': 'All Statuses',
      'search-alerts': 'Search alerts...',
      'apply-filters': 'Apply Filters',
      'clear-all': 'Clear All',
      'no-alerts-found': 'No Alerts Found',
      'no-alerts-message': 'No alerts match your current filters. Try adjusting your search criteria.',
      'bulk-actions': 'Bulk Actions',
      'export-report': 'Export Report',
      'refresh-data': 'Refresh Data',
      'back-to-dashboard': 'Back to Dashboard',
      'showing-alerts': 'Showing',
      'of-alerts': 'of',
      'alerts-total': 'alerts',
      previous: 'Previous',
      next: 'Next',
      
      // Alert/Home UI elements (NEW)
      'settings-title': 'Alert Threshold Settings',
      'settings-close': '×',
      'settings-air-light': 'Air & Light Conditions',
      'settings-temp-range': 'Temperature Range (°C)',
      'settings-min': 'Min',
      'settings-max': 'Max',
      'settings-light-min': 'Minimum Light Intensity (Lux)',
      'settings-soil-ground': 'Soil Conditions',
      'settings-humidity-range': 'Soil Humidity Range (%)',
      'settings-soil-temp-range': 'Soil Temp Range (°C)',
      'reset-defaults': 'Reset Defaults',
      'cancel-btn': 'Cancel',
      'save-changes': 'Save Changes',
      'alert-generated-at': 'Alert generated at',
      'min-ago': 'min ago',
      'unknown-time': 'Unknown time',
      'no-history': 'No recent alert history. System has been stable.',
      'resolve-btn': 'Resolve',
      'critical-immediate': 'critical alerts require immediate attention',
      'low-alert-volume': 'Low alert volume indicates stable system operation',
      'higher-alert-volume': 'Higher alert volume detected - monitor system closely',

      // Alert statuses and types
      'alert-critical': 'Critical',
      'alert-high': 'High',
      'alert-medium': 'Medium',
      'alert-low': 'Low',
      'alert-active': 'Active',
      'alert-resolved': 'Resolved',
      'alert-acknowledged': 'Acknowledged',

      // Common UI elements
      'modal-close': '×',
      loading: 'Loading...',
      error: 'Error',
      success: 'Success',
      warning: 'Warning',
      info: 'Information',
      'try-again': 'Try Again',
      cancel: 'Cancel',
      confirm: 'Confirm',
      'are-you-sure': 'Are you sure?',

      // Strawberry project content
      'hero-title': 'Strawberry Farm Innovation',
      'hero-subtitle': 'Revolutionizing premium strawberry cultivation through smart environmental sensing technology',
      'about-title': 'About the Project',
      'about-text': 'MIGAKI-ICHIGO represents the pinnacle of strawberry cultivation, and our project aims to push the boundaries further with cutting-edge monitoring technology.',
      'challenge-title': 'The Challenge',
      'challenge-text': 'Nursery greenhouses lack adequate monitoring systems, creating blind spots in the cultivation process that affect yield and quality.',
      'solution-title': 'Our Solution',
      'solution-text': 'Compact, wireless environmental sensors that provide real-time data on critical growth factors without disrupting operations.',
      'impact-title': 'The Impact',
      'impact-text': 'Increased yields, improved quality, and data-driven decision making for strawberry farmers.',
      'tech-title': 'Technical Challenges',
      'wireless-title': 'Wireless Communication',
      'wireless-text': 'Overcoming steel structure interference to maintain reliable data transmission up to 2km.',
      'durability-title': 'Durability',
      'durability-text': 'Creating waterproof housings that withstand harsh greenhouse conditions.',
      'data-title': 'Data Integrity',
      'data-text': 'Ensuring continuous monitoring with offline data retention capabilities.',
      'prototype-title': 'Our Prototype',
      'prototype-text': 'The current iteration of our environmental sensing device blends seamlessly into strawberry seedling trays while collecting critical growth data.',
      'feature-1': 'Compact, unobtrusive design',
      'feature-2': 'Multi-sensor array',
      'feature-3': 'Long-range communication',
      'feature-4': 'Weather-resistant housing',
      'achievements-title': 'Expected Achievements',
      'achievements-text': 'By implementing our solution, we aim to increase strawberry yields by 20-30% while improving quality consistency and reducing resource waste.',
      'steps-title': 'Next Steps',
      'step1-title': 'Field Testing',
      'step1-text': 'Real-world validation in nursery environments',
      'step2-title': 'Algorithm Refinement',
      'step2-text': 'Enhancing data analysis for actionable insights',
      'step3-title': 'Farmer Interface',
      'step3-text': 'Developing intuitive dashboards',
      'step4-title': 'Communication Reliability',
      'step4-text': 'Ensuring robust long-distance transmission',

      // Smart Tips
      'tip-water-morning': 'Water your strawberries early in the morning (6-8 AM) to minimize evaporation and prevent leaf burn during peak sun hours.',
      'tip-soil-moisture': 'Maintain soil moisture between 30-70% for optimal strawberry growth.',
      'tip-temp-monitor': 'Monitor temperature closely - strawberries prefer 18-24°C during the day.',
      'tip-light-exposure': 'Ensure adequate light exposure - strawberries need at least 6 hours of sunlight daily.',
      'tip-check-humidity': 'Check soil humidity regularly to prevent root rot and ensure proper nutrition uptake.',

      // Form Labels
      'Start Date': 'Start Date',
      'End Date': 'End Date',
      'Submit': 'Submit',

      // Summary Table Headers
      'Max Temp': 'Max Temp',
      'Min Temp': 'Min Temp',
      'Daily Avg Temp': 'Daily Avg Temp',
      'Daytime Avg Temp': 'Daytime Avg Temp',
      'Nighttime Avg Temp': 'Nighttime Avg Temp',
      'Max Soil Temp': 'Max Soil Temp',
      'Min Soil Temp': 'Min Soil Temp',
      'Daily Avg Soil Temp': 'Daily Avg Soil Temp',
      'Daytime Avg Soil Temp': 'Daytime Avg Soil Temp',
      'Nighttime Avg Soil Temp': 'Nighttime Avg Soil Temp',
      'Max Humidity': 'Max Humidity',
      'Min Humidity': 'Min Humidity',
      'Daily Avg Humidity': 'Daily Avg Humidity',
      'Daytime Avg Humidity': 'Daytime Avg Humidity',
      'Nighttime Avg Humidity': 'Nighttime Avg Humidity',
      'Max Soil Humidity': 'Max Soil Humidity',
      'Min Soil Humidity': 'Min Soil Humidity',
      'Daily Avg Soil Humidity': 'Daily Avg Soil Humidity',
      'Daytime Avg Soil Humidity': 'Daytime Avg Soil Humidity',
      'Nighttime Avg Soil Humidity': 'Nighttime Avg Soil Humidity',
      'Max Light Intensity': 'Max Light Intensity',
      'Daily Avg Light Intensity': 'Daily Avg Light Intensity',
      
      // Summary Labels (Home Page)
      'Min Temperature': 'Min Temperature',
      'Max Temperature': 'Max Temperature',
      'Min Soil Temp': 'Min Soil Temp',
      'Max Soil Temp': 'Max Soil Temp',
      'Min Humidity': 'Min Humidity',
      'Max Humidity': 'Max Humidity',
      'Min Soil Humidity': 'Min Soil Humidity',
      'Max Soil Humidity': 'Max Soil Humidity',
      'Min Light Intensity': 'Min Light Intensity',
      'Max Light Intensity': 'Max Light Intensity',
      'Temperature': 'Temperature',
      'Soil Temp': 'Soil Temp',
      'Humidity': 'Humidity',
      'Soil Humidity': 'Soil Humidity',
      'Light Intensity': 'Light Intensity',

      // Analysis Charts
      'Temperature Analysis': 'Temperature Analysis',
      'Soil Temperature Analysis': 'Soil Temperature Analysis',
      'Humidity Analysis': 'Humidity Analysis',
      'Soil Humidity Analysis': 'Soil Humidity Analysis',
      'Light Intensity Analysis': 'Light Intensity Analysis',
      'Hourly (Today)': 'Hourly (Today)',
      'Daytime Avg (Weekly)': 'Daytime Avg (Weekly)',
      'Nighttime Avg (Weekly)': 'Nighttime Avg (Weekly)',
      '24-Hour Avg (Weekly)': '24-Hour Avg (Weekly)',
      'Daytime Temperature': 'Daytime Temperature',
      'Nighttime Temperature': 'Nighttime Temperature',
      '24-Hour Temperature': '24-Hour Temperature',
      'Daytime Soil Temp': 'Daytime Soil Temp',
      'Nighttime Soil Temp': 'Nighttime Soil Temp',
      '24-Hour Soil Temp': '24-Hour Soil Temp',
      'Daytime Humidity': 'Daytime Humidity',
      'Nighttime Humidity': 'Nighttime Humidity',
      '24-Hour Humidity': '24-Hour Humidity',
      'Daytime Soil Humidity': 'Daytime Soil Humidity',
      'Nighttime Soil Humidity': 'Nighttime Soil Humidity',
      '24-Hour Soil Humidity': '24-Hour Soil Humidity',
      'Daytime Light Intensity': 'Daytime Light Intensity',
      'Nighttime Light Intensity': 'Nighttime Light Intensity',
      '24-Hour Light Intensity': '24-Hour Light Intensity',

      // Footer
      'footer-device-name': 'Small Environmental Sensing Device for Strawberry Production',
      'footer-team-id': 'Team ID',
      'footer-company': 'Company',
      'footer-engineer': 'Engineer',
      'footer-supervisor': 'Supervisor',
      'footer-copyright': '© 2025 GRA Inc. All rights reserved.',

      // Alert Messages
      'alert-temp-high': 'High temperature alert: {0}°C',
      'alert-temp-low': 'Low temperature alert: {0}°C',
      'alert-ground-temp-high': 'High Soil Temp: {0}°C',
      'alert-ground-temp-low': 'Low Soil Temp: {0}°C',
      'alert-soil-moisture-low': 'Low Soil Humidity: {0}%',
      'alert-soil-moisture-high': 'High Soil Humidity: {0}%',
      'alert-light-low': 'Low light conditions: {0} Lux',
      'alert-connection': 'Sensor connection issue - last data received {0} minutes ago',

      // Categories & Status
      'temperature': 'Temperature',
      'moisture': 'Moisture',
      'lighting': 'Lighting',
      'system': 'System',
      'general': 'General',
      'online': 'Online',
      'offline': 'Offline',
      'N/A': 'N/A',
      
      // Title Case Variants (for UI display)
      'Temperature': 'Temperature',
      'Moisture': 'Moisture',
      'Lighting': 'Lighting',
      'System': 'System',
      'General': 'General',
      'Active': 'Active',
      'Resolved': 'Resolved',
      'Critical': 'Critical',
      'Warning': 'Warning',
      'Info': 'Info'
    },
    
    ja: {
      // Base template translations
      title: 'いちごセンサー',
      'nav-home': 'ホーム',
      'nav-measurements': '測定',
      'nav-summary': '概要',
      'nav-analysis': '分析',
      'nav-alert-history': 'アラート履歴',
      footer: 'フッターコンテンツ',

      // Home page translations
      'dashboard-title': 'いちご監視ダッシュボード',
      'dashboard-subtitle': 'リアルタイム環境監視と分析',
      'current-conditions': '現在の環境状況',
      'last-updated': '最終更新:',
      'air-temperature': '気温',
      'air-humidity': '湿度',
      'soil-moisture': '土壌水分',
      'light-intensity': '光の強さ',
      'ground-temp': '地温',
      'active-alerts': 'アクティブアラート',
      'no-alerts': 'アクティブなアラートはありません。すべてのシステムが正常に動作しています。',
      'recent-alert-history': '最近のアラート履歴',
      'view-full-history': '完全な履歴を表示',
      'todays-summary': '今日の概要',
      'min-air-temp': '最低気温',
      'max-air-temp': '最高気温',
      'min-humidity': '最低湿度',
      'max-humidity': '最高湿度',
      'min-light': '最低光量',
      'max-light': '最高光量',
      'min-ground-temp': '最低地温',
      'max-ground-temp': '最高地温',
      'min-soil-moisture': '最低土壌水分',
      'max-soil-moisture': '最高土壌水分',
      'show-more': 'もっと見る',
      'show-less': '閉じる',
      'readings-collected': '件の測定値を今日収集',
      'alert-analytics': 'アラート分析',
      'most-common-issue': '最も一般的な問題',
      'critical-alerts-24h': '重要アラート（24時間）',
      'system-reliability': 'システム信頼性',
      'response-time': '応答時間',
      'quick-actions': 'クイックアクション',
      'view-detailed-data': '詳細データを表示',
      'analytics-dashboard': '分析ダッシュボード',
      'download-report': 'レポートダウンロード',
      'refresh-now': '今すぐ更新',
      'smart-tip': 'スマートヒント',
      'system-online': 'すべてのシステムが動作中',
      'system-offline': 'システムオフライン - 最近のデータなし',
      'attention-required': 'アクティブアラート - 注意が必要',
      'alerts-24h': 'アラート（24時間）',
      'active-alerts-count': 'アクティブアラート',
      'resolved-24h': '解決済み（24時間）',
      'avg-resolution': '平均解決時間',
      'data-fresh': 'データは新鮮です',
      'data-stale': 'データは古いです',
      'next-refresh': '次の更新まで:',
      'sensor-data-updates': 'センサーデータは5分ごとに自動更新されます',

      // Table page translations
      'measurementsFor': 'の測定値',
      'todayMeasurements': '今日の測定値',
      'selectDate': '日付を選択:',
      apply: '適用',
      'showToday': '今日を表示',
      filterByDate: '日付でフィルター:',
      showAll: 'すべて表示',
      filterValuePlaceholder: 'フィルター値',
      headerDate: '日付',
      headerTime: '時間',
      headerTemperature: '温度（°C）',
      'headerSoilTemperature': '地温', // NEW
      headerHumidity: '湿度（%）',
      headerGroundTemperature: '地温（°C）',
      'headerSoilHumidity': '地中湿度', // NEW
      headerLightIntensity: '光の強さ（Lux）',
      downloadTitle: 'データをエクスポート',
      downloadBtn: 'CSVをダウンロード',
      quickStats: 'クイック統計',
      totalRecords: '総レコード数:',
      timeRange: '時間範囲:',
      searchPlaceholder: 'すべての列を検索...',
      lengthMenu: '_MENU_ 件を表示',
      info: '_TOTAL_ 件中 _START_ から _END_ を表示',

      // Summary page translations
      category: 'カテゴリ',
      metric: '指標',
      categories: {
        temperature: '気温（°C）',
        humidity: '湿度（%）',
        light: '光の強さ',
        groundTemp: '地温（°C）',
        groundHumidity: '地中湿度（%）'
      },
      metrics: {
        max: '最大',
        min: '最小',
        dailyAvg: '1日平均',
        daytimeAvg: '日中平均',
        nighttimeAvg: '夜間平均'
      },

      // Analysis page translations
      'analysis-daily-title': '今日の環境データ分析',
      'analysis-weekly-title': '今週の環境データ分析',
      'analysis-temp': '温度パターン',
      'analysis-humidity': '湿度パターン',
      'analysis-light': '光の強さパターン',
      'analysis-day-avg-temp': '日中温度',
      'analysis-day-avg-humidity': '日中湿度',
      'analysis-day-avg-light': '日中光強度',
      'analysis-night-avg-temp': '夜間温度',
      'analysis-night-avg-humidity': '夜間湿度',
      'analysis-night-avg-light': '夜間光強度',
      'analysis-whole-avg-temp': '24時間温度',
      'analysis-whole-avg-humidity': '24時間湿度',
      'analysis-whole-avg-light': '24時間光強度',
      
      // Analysis Chart Titles (NEW)
      'Temperature Analysis': '温度分析',
      'Soil Temperature Analysis': '地温分析',
      'Humidity Analysis': '湿度分析',
      'Soil Humidity Analysis': '土壌湿度分析',
      'Light Intensity Analysis': '光強度分析',
      'Hourly (Today)': '1時間ごと (今日)',
      'Daytime Avg (Weekly)': '日中平均 (週間)',
      'Nighttime Avg (Weekly)': '夜間平均 (週間)',
      '24-Hour Avg (Weekly)': '24時間平均 (週間)',

      // Alert History page translations
      'alert-history-title': 'アラート履歴',
      'alert-history-subtitle': '包括的なアラート追跡と分析',
      'total-24h': '合計（24時間）',
      'resolved-24h-label': '解決済み（24時間）',
      'avg-resolution-label': '平均解決時間',
      'alert-type': 'アラートタイプ',
      'all-types': 'すべてのタイプ',
      'alert-category': 'カテゴリ',
      'all-categories': 'すべてのカテゴリ',
      'alert-severity': '重要度',
      'all-severities': 'すべての重要度',
      'alert-status': 'ステータス',
      'all-statuses': 'すべてのステータス',
      'search-alerts': 'アラートを検索...',
      'apply-filters': 'フィルターを適用',
      'clear-all': 'すべてクリア',
      'no-alerts-found': 'アラートが見つかりません',
      'no-alerts-message': '現在のフィルターに一致するアラートがありません。検索条件を調整してみてください。',
      'bulk-actions': '一括アクション',
      'export-report': 'レポートをエクスポート',
      'refresh-data': 'データを更新',
      'back-to-dashboard': 'ダッシュボードに戻る',
      'showing-alerts': '表示中',
      'of-alerts': '/',
      'alerts-total': 'アラート',
      previous: '前へ',
      next: '次へ',
      
      // Alert/Home UI elements (NEW)
      'settings-title': 'アラートしきい値設定',
      'settings-close': '×',
      'settings-air-light': '気温と光の条件',
      'settings-temp-range': '温度範囲（°C）',
      'settings-min': '最小',
      'settings-max': '最大',
      'settings-light-min': '最低光強度（Lux）',
      'settings-soil-ground': '土壌の状態',
      'settings-humidity-range': '土壌湿度範囲（%）',
      'settings-soil-temp-range': '地温範囲（°C）',
      'reset-defaults': 'デフォルトに戻す',
      'cancel-btn': 'キャンセル',
      'save-changes': '変更を保存',
      'alert-generated-at': 'アラート発生時刻',
      'min-ago': '分前',
      'unknown-time': '不明な時刻',
      'no-history': '最近のアラート履歴はありません。システムは安定しています。',
      'resolve-btn': '解決',
      'critical-immediate': '件の重要アラートに直ちに注意が必要です',
      'low-alert-volume': 'アラート量が少ないため、システムは安定しています',
      'higher-alert-volume': 'アラート量が増加しています - システムを注意深く監視してください',

      // Alert statuses and types
      'alert-critical': '重要',
      'alert-high': '高',
      'alert-medium': '中',
      'alert-low': '低',
      'alert-active': 'アクティブ',
      'alert-resolved': '解決済み',
      'alert-acknowledged': '確認済み',

      // Common UI elements
      'modal-close': '×',
      loading: '読み込み中...',
      error: 'エラー',
      success: '成功',
      warning: '警告',
      info: '情報',
      'try-again': '再試行',
      cancel: 'キャンセル',
      confirm: '確認',
      'are-you-sure': '本当によろしいですか？',

      // Strawberry project content
      'hero-title': 'いちご農園の革新',
      'hero-subtitle': 'スマート環境センシング技術による高級いちご栽培の革新',
      'about-title': 'プロジェクトについて',
      'about-text': 'ミガキイチゴはいちご栽培の頂点を表し、私たちのプロジェクトは最先端の監視技術でその限界をさらに押し広げることを目指しています。',
      'challenge-title': '課題',
      'challenge-text': '育苗用温室には適切な監視システムが不足しており、収量と品質に影響を与える栽培プロセスの盲点が生じています。',
      'solution-title': '私たちの解決策',
      'solution-text': '作業を妨げることなく重要な成長要因に関するリアルタイムデータを提供するコンパクトな無線環境センサー。',
      'impact-title': '影響',
      'impact-text': 'いちご農家の収量増加、品質向上、データに基づく意思決定。',
      'tech-title': '技術的課題',
      'wireless-title': '無線通信',
      'wireless-text': '鋼構造物の干渉を克服し、2kmまでの信頼性のあるデータ伝送を維持。',
      'durability-title': '耐久性',
      'durability-text': '過酷な温室条件に耐える防水ケースの作成。',
      'data-title': 'データの完全性',
      'data-text': 'オフライン時のデータ保持機能を備えた継続的な監視の確保。',
      'prototype-title': '私たちのプロトタイプ',
      'prototype-text': '現在の環境センシングデバイスの反復は、重要な成長データを収集しながら、いちごの苗トレイにシームレスに溶け込みます。',
      'feature-1': 'コンパクトで目立たないデザイン',
      'feature-2': 'マルチセンサーアレイ',
      'feature-3': '長距離通信',
      'feature-4': '耐候性ハウジング',
      'achievements-title': '期待される成果',
      'achievements-text': '私たちのソリューションを実装することで、いちごの収量を20-30％増加させ、品質の一貫性を向上させ、資源の浪費を減らすことを目指しています。',
      'steps-title': '次のステップ',
      'step1-title': 'フィールドテスト',
      'step1-text': '育苗環境での実世界での検証',
      'step2-title': 'アルゴリズムの改良',
      'step2-text': '実用的な洞察のためのデータ分析の強化',
      'step3-title': '農家向けインターフェース',
      'step3-text': '直感的なダッシュボードの開発',
      'step4-title': '通信の信頼性',
      'step4-text': '堅牢な長距離伝送の確保',

      // Smart Tips
      'tip-water-morning': 'いちごへの水やりは、蒸発を最小限に抑え、日中のピーク時の葉焼けを防ぐために、早朝（午前6時〜8時）に行いましょう。',
      'tip-soil-moisture': 'いちごの最適な成長のために、土壌水分を30〜70％の間に保ちましょう。',
      'tip-temp-monitor': '温度を注意深く監視してください。いちごは日中18〜24°Cを好みます。',
      'tip-light-exposure': '適切な光量を確保してください。いちごは毎日少なくとも6時間の日光を必要とします。',
      'tip-check-humidity': '根腐れを防ぎ、適切な栄養吸収を確保するために、土壌湿度を定期的に確認してください。',

      // Form Labels
      'Start Date': '開始日',
      'End Date': '終了日',
      'Submit': '送信',

      // Summary Table Headers
      'Max Temp': '最高気温',
      'Min Temp': '最低気温',
      'Daily Avg Temp': '日平均気温',
      'Daytime Avg Temp': '日中平均気温',
      'Nighttime Avg Temp': '夜間平均気温',
      'Max Soil Temp': '最高地温',
      'Min Soil Temp': '最低地温',
      'Daily Avg Soil Temp': '日平均地温',
      'Daytime Avg Soil Temp': '日中平均地温',
      'Nighttime Avg Soil Temp': '夜間平均地温',
      'Max Humidity': '最高湿度',
      'Min Humidity': '最低湿度',
      'Daily Avg Humidity': '日平均湿度',
      'Daytime Avg Humidity': '日中平均湿度',
      'Nighttime Avg Humidity': '夜間平均湿度',
      'Max Soil Humidity': '最高土壌湿度',
      'Min Soil Humidity': '最低土壌湿度',
      'Daily Avg Soil Humidity': '日平均土壌湿度',
      'Daytime Avg Soil Humidity': '日中平均土壌湿度',
      'Nighttime Avg Soil Humidity': '夜間平均土壌湿度',
      'Max Light Intensity': '最高光強度',
      'Daily Avg Light Intensity': '日平均光強度',
      
      // Summary Labels (Home Page)
      'Min Temperature': '最低気温',
      'Max Temperature': '最高気温',
      'Min Soil Temp': '最低地温',
      'Max Soil Temp': '最高地温',
      'Min Humidity': '最低湿度',
      'Max Humidity': '最高湿度',
      'Min Soil Humidity': '最低土壌湿度',
      'Max Soil Humidity': '最高土壌湿度',
      'Min Light Intensity': '最低光強度',
      'Max Light Intensity': '最高光強度',
      'Temperature': '気温',
      'Soil Temp': '地温',
      'Humidity': '湿度',
      'Soil Humidity': '土壌湿度',
      'Light Intensity': '光強度',

      // Analysis Charts
      'Temperature Analysis': '温度分析',
      'Soil Temperature Analysis': '地温分析',
      'Humidity Analysis': '湿度分析',
      'Soil Humidity Analysis': '土壌湿度分析',
      'Light Intensity Analysis': '光強度分析',
      'Hourly (Today)': '1時間ごと (今日)',
      'Daytime Avg (Weekly)': '日中平均 (週間)',
      'Nighttime Avg (Weekly)': '夜間平均 (週間)',
      '24-Hour Avg (Weekly)': '24時間平均 (週間)',
      'Daytime Temperature': '日中気温',
      'Nighttime Temperature': '夜間気温',
      '24-Hour Temperature': '24時間気温',
      'Daytime Soil Temp': '日中地温',
      'Nighttime Soil Temp': '夜間地温',
      '24-Hour Soil Temp': '24時間地温',
      'Daytime Humidity': '日中湿度',
      'Nighttime Humidity': '夜間湿度',
      '24-Hour Humidity': '24時間湿度',
      'Daytime Soil Humidity': '日中土壌湿度',
      'Nighttime Soil Humidity': '夜間土壌湿度',
      '24-Hour Soil Humidity': '24時間土壌湿度',
      'Daytime Light Intensity': '日中光強度',
      'Nighttime Light Intensity': '夜間光強度',
      '24-Hour Light Intensity': '24時間光強度',

      // Footer
      'footer-device-name': 'いちご生産用小型環境センシングデバイス',
      'footer-team-id': 'チームID',
      'footer-company': '会社名',
      'footer-engineer': 'エンジニア',
      'footer-supervisor': 'スーパーバイザー',
      'footer-copyright': '© 2025 GRA Inc. All rights reserved.',

      // Alert Messages
      'alert-temp-high': '高温アラート: {0}°C',
      'alert-temp-low': '低温アラート: {0}°C',
      'alert-ground-temp-high': '地温高温: {0}°C',
      'alert-ground-temp-low': '地温低温: {0}°C',
      'alert-soil-moisture-low': '土壌低湿度: {0}%',
      'alert-soil-moisture-high': '土壌高湿度: {0}%',
      'alert-light-low': '低照度: {0} Lux',
      'alert-connection': 'センサー接続エラー - 最後のデータ受信から {0} 分経過',

      // Categories & Status
      'temperature': '温度',
      'moisture': '湿度',
      'lighting': '照明',
      'system': 'システム',
      'general': '一般',
      'online': 'オンライン',
      'offline': 'オフライン',
      'N/A': 'データなし',

      // Title Case Variants (for UI display)
      'Temperature': '温度',
      'Moisture': '湿度',
      'Lighting': '照明',
      'System': 'システム',
      'General': '一般',
      'Active': 'アクティブ',
      'Resolved': '解決済み',
      'Critical': '重要',
      'Warning': '警告',
      'Info': '情報'
    }
  };

  // --- Utility Functions ---

  /**
   * Safely retrieves a nested value from an object using a dot-separated key.
   * @param {object} obj - The translation dictionary (e.g., translations.ja).
   * @param {string} key - The dot-separated key (e.g., 'categories.temperature').
   * @returns {*} The value, or undefined if not found.
   */
  function getNestedValue(obj, key) {
    // Avoids errors if obj or parts of the path are null/undefined
    return key.split('.').reduce((o, k) => (o && o[k] !== undefined) ? o[k] : undefined, obj);
  }

  /**
   * Interpolates placeholder values ({0}, {1}, etc.) into a string.
   * @param {string} template - The translated string with placeholders.
   * @param {string[]} args - An array of arguments to substitute.
   * @returns {string} The final, interpolated string.
   */
  function interpolate(template, args = []) {
    return args.reduce((str, arg, i) => str.replace(new RegExp(`\\{${i}\\}`, 'g'), arg), template);
  }

  /**
   * Updates the content or attribute of a single HTML element.
   * @param {HTMLElement} el - The element to update.
   * @param {string} value - The translated string.
   * @param {string[]} args - Interpolation arguments.
   */
  function updateElementContent(el, value, args = []) {
    let content = interpolate(value, args);

    if (el.tagName === 'INPUT' && (el.type === 'text' || el.type === 'search' || el.type === 'password' || el.type === 'date')) {
      // Handles placeholder text for input fields
      el.placeholder = content;
    } else if (el.tagName === 'IMG') {
      // Handles alt text for images
      el.alt = content;
    } else if (el.tagName === 'META' && el.getAttribute('name') === 'description') {
      // Handles meta tags
      el.content = content;
    } else if (el.dataset.i18nAttr) {
        // Handle custom attributes specified via data-i18n-attr="title"
        el.setAttribute(el.dataset.i18nAttr, content);
    } else {
      // Handles text content for all other elements (h1, span, p, button, etc.)
      el.textContent = content;
    }
  }

  /**
   * Updates DataTables specific UI elements.
   * NOTE: This requires DataTables to be initialized BEFORE this function runs.
   * @param {object} dict - The current language dictionary.
   */
  function updateDataTableUI(dict) {
    // Use the global jQuery/DataTables object check
    if (!window.jQuery || !$.fn.DataTable) {
      // console.warn('DataTables library not found. Skipping UI update.');
      return;
    }
    
    const table = $('#measurements-table');
    if (!$.fn.DataTable.isDataTable(table)) return;

    try {
      // Use the settings method to update language options on existing table
      table.DataTable().settings()[0].oLanguage = {
        sSearch: dict.searchPlaceholder, // Updated search label
        sLengthMenu: dict.lengthMenu,   // Updated length menu text
        sInfo: dict.info                // Updated info text
      };
      
      // Redraw the table to apply changes (optional, but often needed)
      table.DataTable().draw(); 

    } catch (e) {
      console.error('DataTables language update failed:', e);
    }
  }


  // --- Core Language Logic ---

  /**
   * Main function to set the language across the entire application UI.
   * @param {string} lang - The language code (e.g., 'en', 'ja').
   * @param {HTMLElement} [root=document] - The DOM element to start the search from (for partial updates).
   */
  window.setLanguage = function (lang, root = document) {
    // Expose translations for use in other scripts (like home.html)
    window.translations = translations; 
    
    const dict = translations[lang] || translations.en;
    document.documentElement.lang = lang; // Update HTML lang attribute

    // 1. Iterate through all translatable elements
    root.querySelectorAll('[data-i18n]').forEach(el => {
      let key = el.getAttribute('data-i18n');
      let args = [];
      
      // Handle keys with arguments (e.g., "alert-temp-high|28.5")
      if (key && key.includes('|')) {
        const parts = key.split('|');
        key = parts[0];
        args = parts.slice(1);
      }

      let value = getNestedValue(dict, key);
      
      // Fallback to English if translation is missing (or use a placeholder)
      if (value === undefined) {
          const fallbackDict = translations.en;
          value = getNestedValue(fallbackDict, key);
      }
      
      if (value !== undefined) {
        updateElementContent(el, value, args);
      } else {
          // console.warn(`Translation key not found: ${key} in language ${lang}`);
      }
    });

    // 2. Update library-specific elements (like DataTables)
    updateDataTableUI(dict);
  }

  // --- Initialization ---
  
  const languageSelect = document.getElementById('language-select') || document.querySelector('.language-selector select');

  if (languageSelect) {
    const savedLang = localStorage.getItem('preferredLanguage') || 'en';
    languageSelect.value = savedLang;
    
    // Initial translation on page load
    window.setLanguage(savedLang);

    // Event listener for language change
    languageSelect.addEventListener('change', e => {
      const lang = e.target.value;
      localStorage.setItem('preferredLanguage', lang);
      window.setLanguage(lang);
    });
  } else {
      const defaultLang = localStorage.getItem('preferredLanguage') || 'en';
      window.setLanguage(defaultLang);
      // console.warn('Language selector element not found. Using default language settings.');
  }

});