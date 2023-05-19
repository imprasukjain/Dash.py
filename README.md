# FMP API Stock Dashboard with Email Feature

This repository contains a stock dashboard application built with the Dash module in Python, using the Financial Modeling Prep (FMP) API to fetch stock data. It also includes an email feature that utilizes a Google account to send email notifications.

## Features

- View real-time stock data from the FMP API
- Email feature to receive stock data updates

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python (version 3.7 or above)
- Dash (version 1.20.0 or above)
- Requests (version 2.26.0 or above)
- Pandas (version 1.3.4 or above)
- Google Account credentials (for email feature)

## Setup

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/imprasukjain/dash.py.git
   ```

2. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

3. Obtain an API key from the Financial Modeling Prep (FMP) website by signing up for an account (if you haven't already). This key will be used to access the stock data.

4. Enable the Gmail API for your Google Account and create a new OAuth 2.0 client ID to obtain the necessary credentials for sending emails. Refer to the [Gmail API documentation](https://developers.google.com/gmail/api/quickstart/python) for detailed instructions on how to set this up.

5. Place your FMP API key and Gmail credentials in the  file provided. Update the following variables with your respective values:



## Usage

To start the application, run the following command:

```shell
python app.py
```

This will start a local server, and you can access the stock dashboard by visiting `http://localhost:8050` in your web browser.

Use the interface to search for stocks, view their real-time data, and explore various visualizations. You can also configure the email feature to receive stock data updates by providing your email address and selecting the desired frequency of updates.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.
<a href="mailto:p.jain161202@gmail.com">Contact me !</a>


## Acknowledgements

- [Financial Modeling Prep](https://financialmodelingprep.com/) - Providing the API for stock data
- [Plotly Dash](https://dash.plotly.com/) - Interactive Python framework for building web applications
- [Google API Python Client](https://developers.google.com/api-client-library/python) - Python library for accessing Google APIs
