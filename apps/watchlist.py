import streamlit as st
import streamlit.components.v1 as components

def app():
  
  components.html(f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/markets/" rel="noopener" target="_blank"><span class="blue-text">Financial Markets</span></a> by TradingView</div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-quotes.js" async>
      {
      "width": 770,
      "height": 450,
      "symbolsGroups": [
        {
          "name": "UPCOM",
          "originalName": "Indices",
          "symbols": [
            {
              "name": "UPCOM:VTP"
            },
            {
              "name": "HNX:KLF"
            },
            {
              "name": "UPCOM:ABB"
            },
            {
              "name": "HOSE:AMD"
            }
          ]
        },
        {
          "name": "Futures",
          "originalName": "Futures",
          "symbols": [
            {
              "name": "CME_MINI:ES1!",
              "displayName": "S&P 500"
            },
            {
              "name": "CME:6E1!",
              "displayName": "Euro"
            },
            {
              "name": "COMEX:GC1!",
              "displayName": "Gold"
            },
            {
              "name": "NYMEX:CL1!",
              "displayName": "Crude Oil"
            },
            {
              "name": "NYMEX:NG1!",
              "displayName": "Natural Gas"
            },
            {
              "name": "CBOT:ZC1!",
              "displayName": "Corn"
            }
          ]
        },
        {
          "name": "Bonds",
          "originalName": "Bonds",
          "symbols": [
            {
              "name": "CME:GE1!",
              "displayName": "Eurodollar"
            },
            {
              "name": "CBOT:ZB1!",
              "displayName": "T-Bond"
            },
            {
              "name": "CBOT:UB1!",
              "displayName": "Ultra T-Bond"
            },
            {
              "name": "EUREX:FGBL1!",
              "displayName": "Euro Bund"
            },
            {
              "name": "EUREX:FBTP1!",
              "displayName": "Euro BTP"
            },
            {
              "name": "EUREX:FGBM1!",
              "displayName": "Euro BOBL"
            }
          ]
        },
        {
          "name": "Forex",
          "originalName": "Forex",
          "symbols": [
            {
              "name": "FX:EURUSD"
            },
            {
              "name": "FX:GBPUSD"
            },
            {
              "name": "FX:USDJPY"
            },
            {
              "name": "FX:USDCHF"
            },
            {
              "name": "FX:AUDUSD"
            },
            {
              "name": "FX:USDCAD"
            }
          ]
        }
      ],
      "showSymbolLogo": true,
      "colorTheme": "light",
      "isTransparent": false,
      "locale": "en"
    }
      </script>
    </div>
    <!-- TradingView Widget END -->
""", width=520)