
var xmlHttp = new XMLHttpRequest();
var dataText = "I want to die right now"
dataText = encodeURIComponent(dataText.trim())
console.log(dataText);
xmlHttp.open("GET", "https://watson-api-explorer.mybluemix.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text=" + dataText + "&features=sentiment&return_analyzed_text=false&clean=true&fallback_to_raw=true&concepts.limit=8&emotion.document=true&entities.limit=50&entities.emotion=false&entities.sentiment=false&keywords.limit=50&keywords.emotion=false&keywords.sentiment=false&relations.model=en-news&semantic_roles.limit=50&semantic_roles.entities=false&semantic_roles.keywords=false&sentiment.document=true", false); // true for asynchronous
xmlHttp.send();

 var file = "file://trumpData.txt"
var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                console.log(allText);
            }
        }
    }
    rawFile.send(null);



//Let's say the /me endpoint on the provider API returns a JSON object
//with the field "name" containing the name "John Doe"
// OAuth.popup("twitter")
// .done(function(result) {
//     //result.get('/me')
//     result.me()
//     console.log(result)
//     .done(function (response) {
//         //this will display "John Doe" in the console
//         console.log(response.name);
//     })
//     .fail(function (err) {
//         //handle error with err
//     });
// })
// .fail(function (err) {
//     //handle error with err
// });
// console.log(xmlHttp.status)
// console.log(xmlHttp.statusText)
//console.log(xmlHttp.responseText)

// var Stream = require['user-stream'];
// var stream = new Stream({
//     consumer_key: '2BTDpAlRRh1i9mPfgKX8V9Wt4',
//     consumer_secret: 'wlWlQb0XyGOufjapblzSceF5jDNbm6LVlrn8MfDLE3NfJZsuhz',
//     access_token_key: '2588941748-iZa2nzjObbxw960FRtg1zpdTrn176XWjaV4H2WN',
//     access_token_secret: 'c1slEzDClEABP0T5kk59j1OQSUaX2EhBL4WNchvqFQ8KY'
// });
//
// //create stream
// stream.stream();
//
// //listen stream data
// stream.on('data', function(json) {
//   console.log(json);
// });
//
//   	stream.getMentionsTimeline({ count: '10'}, error, success);

// var error = function (err, response, body) {
//     	console.log('ERROR [%s]', err);
// 	};
// 	var success = function (data) {
//     	console.log('Data [%s]', data);
// 	};
//
// 	var Twitter = require['twitter-node-client'].Twitter;
//
//     var twitter = new Twitter();
//
// 	twitter.getMentionsTimeline({ count: '10'}, error, success);
// }

// OAuth.initialize('2588941748-iZa2nzjObbxw960FRtg1zpdTrn176XWjaV4H2WN');
// OAuth.popup('twitter', function(error, success){
//   var twitterHttp = new XMLHttpRequest();
//   var username = "therealdonaldtrump";
//   twitterHttp.open("GET", "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=2", false); // true for asynchronous
//   // twitterHttp.setRequestHeader("Authorization", "OAuth oauth_consumer_key=\"2BTDpAlRRh1i9mPfgKX8V9Wt4\",oauth_token=\"2588941748-iZa2nzjObbxw960FRtg1zpdTrn176XWjaV4H2WN\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1490534520\",oauth_nonce=\"7NGa1XQEpRO\",oauth_version=\"1.0\",oauth_signature=\"fUm3LzkDWRt8kId0ui8aptG9FHM%3D\"");
//   twitterHttp.send();
//   console.log(twitterHttp.statusText);
//   console.log(twitterHttp.responseText);
// });

// OAuth.popup('twitter')
// .done(function(result) {
//     result.get('/me')
//     .done(function (response) {
//         //this will display "John Doe" in the console
//         console.log(response.name);
//     })
//     .fail(function (err) {
//         //handle error with err
//     });
// })
// .fail(function (err) {
//     //handle error with err
// });
// var response = xmlHttp.responseText;
// var obj = JSON.parse(response);
// console.log(obj["sentiment"]["document"]["score"]);
// document.getElementById("riskLikelihood").innerHTML = obj["sentiment"]["document"]["score"];
