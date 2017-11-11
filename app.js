var express = require("express");
var request = require("request");
var querystring = require("querystring");
var cookieParser = require("cookie-parser");

var client_id = "d2160926112f4d9584800ce1caea9d6d";
var client_secret = "f36b08b206804d86833e790e3e0e3052";
var redirect_uri = "http://localhost:8888/callback";

/*
 * generates a random string of numbers and letters
 * @param {number} length - the length of the string
 * @return {string} the generated string
 */
var generateRandomString = function(length) {
  var generated_text = "";
  var possible_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for( var i = 0; i < length; ++i ) {
    generated_text += possible_chars.charAt(Math.floor(Math.random() * possible_chars.length));
  }
  return generated_text;
};

var stateKey = "spotify_auth_state";

var app = express();

app.use(express.static(__dirname + "/public")).use(cookieParser());

app.get("/login", function(req, res) {
  var state = generateRandomString(16);
  res.cookie(stateKey, state);

  //request authorization
  var scope = "user-read-private user-read-email";
  res.redirect("http://accounts.spotify.com/authorize?" + 
      querystring.stringify({
        response_type: "code",
        client_id: client_id,
        scope: scope,
        redirect_uri: redirect_uri,
        state: state
      }));
});

app.get("/callback", function(req, res) {
  //request refresh and access tokens
  var code = req.query.code || null;
  var state = req.query.state || null;
  var storedState = req.cookies ? req.cookies[stateKey]: null;

  if( state === null || state !== storedState) {
    res.redirect("/#" + querystring.stringify({
      error: "state_mismatch"
    }));
  }
  else {
    res.clearCookie(stateKey);
    var authOptions = {
      url: "https://accounts.spotify.com/api/token",
      form: {
        code: code,
        redirect_uri: redirect_uri,
        grant_type: "authorization_code"
      },
      headers: {
        "Authorization": "Basic " + (new Buffer(client_id + ":" + client_secret).toString("base64"))
      },
      json: true
    };

    request.post(authOptions, function(error, response, body) {
      if( !error && response.statusCode === 200 ) {
        var access_token = body.access_token,
          refresh_token = body.refresh_token;

        var options = {
          url: "https://api.spotify.com/v1/me",
          headers: {"Authorization": "Bearer " + access_token},
          json: true
        };

        //use access tokens to access Spotify Web API
        request.get(options, function(error, response, body) {
          console.log(body);
        });

        //pass token to browser to make requests from there
        res.redirect("/#" + querystring.stringify({
          access_token: access_token,
          refresh_token: refresh_token
        }));
      }
      else {
        res.redirect("/#" + querystring.stringify({
          error: "invalid_token"
        }));
      }
    });
  }
});

app.get("/refresh_token", function(req, res) {
  //request access from refresh token
  var refresh_token = req.query.refresh_token;
  var authOptions = {
    url: "https://accounts.spotify.com/api/token",
    headers: {"Authorization": "Basic " + (new Buffer(client_id + ":" + client_secret).toString("base64"))},
    form: {
      grant_type: "refresh_token",
      refresh_token: refresh_token
    },
    json: true
  };

  request.post(authOptions, function(error, response, body) {
    if( !error && response.statusCode === 200 ) {
      var access_token = body.access_token;
      res.send({
        "access_token": access_token
      });
    }
  });
});

console.log("listening on port 8888");
app.listen(8888);

