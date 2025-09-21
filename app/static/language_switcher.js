document.addEventListener('DOMContentLoaded', () => {
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
      headerHumidity: 'Humidity (%)',
      headerLightIntensity: 'Light Intensity (Lux)',
      headerGroundTemperature: 'Ground Temperature (°C)',
      headerGroundHumidity: 'Ground Humidity (%)',
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
      'step4-text': 'Ensuring robust long-distance transmission'
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
      headerHumidity: '湿度（%）',
      headerLightIntensity: '光の強さ（Lux）',
      headerGroundTemperature: '地温（°C）',
      headerGroundHumidity: '地中湿度（%）',
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
      'step4-text': '堅牢な長距離伝送の確保'
    }
  };

  const languageSelect = document.getElementById('language-select') || document.querySelector('.language-selector select');
  if (!languageSelect) return;

  const savedLang = localStorage.getItem('preferredLanguage') || 'en';
  languageSelect.value = savedLang;
  setLanguage(savedLang);

  languageSelect.addEventListener('change', e => {
    const lang = e.target.value;
    localStorage.setItem('preferredLanguage', lang);
    setLanguage(lang);
  });

  function setLanguage(lang) {
    document.documentElement.lang = lang;
    const dict = translations[lang] || translations.en;

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const value = getNestedValue(dict, key);
      if (value !== undefined) updateElementContent(el, value);
    });

    updateDataTableUI(dict);
  }

  function getNestedValue(obj, key) {
    return key.split('.').reduce((o, k) => (o || {})[k], obj);
  }

  function updateElementContent(el, value) {
    if (el.tagName === 'INPUT' && el.type !== 'button' && el.type !== 'submit') {
      el.placeholder = value;
    } else if (el.tagName === 'IMG') {
      el.alt = value;
    } else if (el.tagName === 'META' && el.getAttribute('name') === 'description') {
      el.content = value;
    } else {
      el.textContent = value;
    }
  }

  function updateDataTableUI(dict) {
    if (!window.jQuery || !$.fn.DataTable) return;
    
    const table = $('#measurements-table');
    if (!$.fn.DataTable.isDataTable(table)) return;

    try {
      table.DataTable().language({
        search: dict.searchPlaceholder,
        lengthMenu: dict.lengthMenu,
        info: dict.info
      }).draw();
    } catch (e) {
      console.error('DataTables update failed:', e);
    }
  }
});