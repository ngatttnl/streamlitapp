import streamlit as st
import streamlit.components.v1 as components


stock = "HNX:KLF"
#Mini chart widget
components.html(f"""
    <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Quotes</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
        {{
        "symbol": "{stock}",
        "width": "350",
        "height": "320",
        "locale": "en",
        "dateRange": "12M",
        "colorTheme": "light",
        "trendLineColor": "rgba(41, 98, 255, 1)",
        "underLineColor": "rgba(41, 98, 255, 0.3)",
        "underLineBottomColor": "rgba(41, 98, 255, 0)",
        "isTransparent": false,
        "autosize": false,
        "largeChartUrl": ""
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
    """, width = 350, height=320)

#Symbol Overview Widget
    components.html(f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div id="tradingview_1934a"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{stock}</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.MediumWidget(
    {{
    "symbols": [
        [
        "{stock}|12M"
        ]
    ],
    "chartOnly": false,
    "width": 1000,
    "height": 400,
    "locale": "en",
    "colorTheme": "light",
    "gridLineColor": "rgba(240, 243, 250, 0)",
    "fontColor": "#787B86",
    "isTransparent": false,
    "autosize": false,
    "showFloatingTooltip": true,
    "showVolume": false,
    "scalePosition": "no",
    "scaleMode": "Normal",
    "fontFamily": "Trebuchet MS, sans-serif",
    "noTimeScale": false,
    "chartType": "area",
    "lineColor": "#2962FF",
    "bottomColor": "rgba(41, 98, 255, 0)",
    "topColor": "rgba(41, 98, 255, 0.3)",
    "container_id": "tradingview_1934a"
    }}
    );
    </script>
    </div>
    <!-- TradingView Widget END -->
    """, height=420)
    