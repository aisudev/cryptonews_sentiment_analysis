from FinancialSentiment import FinancialSentiment

if __name__ == '__main__':
    finSent = FinancialSentiment(data_path='./data.csv')
    sent = """The surging DeFi sector has resulted in a mass minting of Tether in 2020 — including $3B last month alone — which has pushed its market capitalization over $15 billion.
At the beginning of the year there was just over $4 billion USDT in circulation, and today that figure is over $15 billion. DeFi has been the driving force behind the Tether mining machine as more and more liquidity pools are based on stablecoins. It was reported that Tether’s average daily transfer value had exceeded that of PayPal late last month as demand for the stablecoin continues to surge.
Tether made the milestone announcement and pointed out that last month the market capitalization has increased by billions more:
Tether has just surpassed a $15 billion market capitalization!

In only one month, Tether’s market cap has increased by more than $3 billion, maintaining its number one spot as the most liquid, stable and trusted currency! pic.twitter.com/MLOWkiIDvF
— Tether (@Tether_to) September 17, 2020
An infographic from Flipsidecrypto.com depicts the movements of Tether between users and exchanges this month. The main centralized exchanges still account for the lion’s share of USDT trade with Binance and Bitfinex holding around $2 billion between them.
Image - flipsidecrypto.com
According to the Tether Transparency Report, the amount of UDST on Ethereum has now increased to over $10 billion, or almost two thirds of the entire supply. There is currently around $4.2 billion on Tron and $1.3 billion circulating on Omni.
Late last month, Tether conducted a billion dollar token swap from Bitfinex to Binance as reported by Cointelegraph. The swap was initiated because Binance had a surplus of $1 billion USDT based on the TRON blockchain and wanted to trade it for the equivalent amount of Ethereum-based Tether.
On September 15, another swap was initiated by Tether as demand for the ERC-20 version of the stablecoin exceeds that of other networks, such as Tron.
Tomorrow Tether will coordinate with a 3rd party to perform two chain swaps (conversion from Tron to ERC20 protocol) for 1B USDt.
Tether total supply will not change during this process.
Read more here: https://t.co/abfgnELSvi
— Tether (@Tether_to) September 14, 2020
However there are ongoing moves to shift Tether transfers onto other networks from Ethereum as gas fees continue to cripple the network. Over the past month USDT has been made available on the Layer 2 OMG Network and launched on the high speed Solana blockchain.
Meanwhile some in the crypto community are still calling for a full audit which will determine whether there are $15 billion real dollars and assets backing up the stablecoin, or the whole thing is a house of cards.
The truth may be revealed as part of the ongoing Tether lawsuit in New York. The Office of the Attorney General (OAG) filed a letter on September 8 which asked for disclosure of financial documents. The lawsuit concerns allegations that Bitfinex had ‘lost’ around $1 billion in customer funds and used Tether reserves to mask the imbalance. Tether and Bitfinex have rejected the lawsuit as baseless.
    """
    pred = finSent.predict(sent)
    print(f"\n\n\n {pred}")
