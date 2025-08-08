# Expense It! -- Gmail Add-ons Codelab
 
 Quickly add expenses from email receipts to a Google Sheet, all without leaving
 Gmail.

 This project is an example of a Gmail add-on, which can extend the Gmail
 interface and communicate with external services. It is written in [Google Apps
 Script](https://developers.google.com/apps-script/).

 The full version of the project is available for public use and can be
 installed from the G Suite Marketplace.

 ## Getting Started

You can follow [this codelab](https://g.co/codelabs/gmail-add-ons) to build a
simplified version of the add-on.


## Usage

 After installing the add-on from the G Suite Marketplace, open Gmail on desktop
 or mobile and find an electronic receipt. Click on the icon vaguely resembling
 a receipt:
 ![receiptPicture](https://www.gstatic.com/images/icons/material/system/1x/receipt_black_24dp.png).
 A form for specifying details about the expense will appear, with the fields
 already filled. Edit as necessary and submit the form, thereby adding
information to a spreadsheet. You can also create a new spreadsheet from within
the add-on.


## Environment Variables

The application reads configuration from the environment. Define these in a
`.env` file or your shell before running the project:

- `SECRET_KEY` – secret used for signing tokens.
- `ALGORITHM` – algorithm used for token generation. Defaults to `HS256`.
- `ACCESS_TOKEN_EXPIRE_MINUTES` – token expiration time in minutes. Defaults to
  `30`.


## License

 This library is licensed under Apache 2.0. Full license text is available in
 [LICENSE](LICENSE).
