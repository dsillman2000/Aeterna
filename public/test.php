<?php
echo "hi";
session_start();
require_once("twitteroauth/twitteroauth/twitteroauth.php"); //Path to twitteroauth library you downloaded in step 3

$twitteruser = "realdonaldtrump"; //user name you want to reference
$notweets = 2; //how many tweets you want to retrieve
$consumerkey = "2BTDpAlRRh1i9mPfgKX8V9Wt4"; //Noted keys from step 2
$consumersecret = "wlWlQb0XyGOufjapblzSceF5jDNbm6LVlrn8MfDLE3NfJZsuhz"; //Noted keys from step 2
$accesstoken = "2588941748-iZa2nzjObbxw960FRtg1zpdTrn176XWjaV4H2WN"; //Noted keys from step 2
$accesstokensecret = "c1slEzDClEABP0T5kk59j1OQSUaX2EhBL4WNchvqFQ8KY"; //Noted keys from step 2

function getConnectionWithAccessToken($cons_key, $cons_secret, $oauth_token, $oauth_token_secret) {
  $connection = new TwitterOAuth($cons_key, $cons_secret, $oauth_token, $oauth_token_secret);
  return $connection;
}

$connection = getConnectionWithAccessToken($consumerkey, $consumersecret, $accesstoken, $accesstokensecret);

$tweets = $connection->get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=".$twitteruser."&count=".$notweets);

echo json_encode($tweets);
echo $tweets; //testing remove for production
?>
