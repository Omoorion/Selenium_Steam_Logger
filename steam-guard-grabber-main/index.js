const reader = require("readline-sync");
const SteamTotp = require("steam-totp");
var SteamUser = require("steam-user");
const ReadLine = require("readline");
var fs = require("fs");

// Instance for account
var firstClient = new SteamUser();

// Config, you must insert your account details and shared secrets in there to proceed.
var config = JSON.parse(fs.readFileSync("./config.json"));

var firstLogonOptions = {
  accountName: config.account.username,
  password: config.account.password,
  twoFactorCode: config.account.shared_secret,
};

console.log("----------------------\nAccount: \n%s - Succesfully logged in");
console.log("%s - Account Name", firstLogonOptions.accountName);
console.log("%s - Account Password", firstLogonOptions.password);
console.log(
  "%s - Account Shared Secret\n----------------------",
  firstLogonOptions.twoFactorCode
);
var guardcode = SteamTotp.getAuthCode(config.account.shared_secret)
console.log(
  `Steam Guard: \n%s - Steam Guard Code [30 Seconds]\n----------------------`,
  guardcode
);
// insert the authenticator code into the .txt file for usage in the main.py function
fileList = 'steamauthcode.txt';

fs.readFile(fileList, function (err, data) {
    if (err) throw err;
    data = guardcode
    fs.writeFile(fileList, data, function (err) {
        err || console.log('Data replaced');
    });
});
