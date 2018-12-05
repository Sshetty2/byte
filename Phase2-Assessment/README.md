# Phase 2 Assessment: Twitter Clone Specification

## Summary

Build a Twitter clone, with a super clever name.

## Specifics

Your app. will have two pages built with templates: A user page and a home page.

Your app. will have many users, and a user will have many tweets.

The home page will have a login form, display every tweet in reverse chronological order and a logout form, but only if a visitor is logged in.

The user page will display all of a user's tweets, and provide a form for a user to add a new tweet.

A user should not need a password or the ability to register to see the tweets on the frontpage.

### Minimum Requirements

- A frontpage renders and displays every tweet.
- Something akin to a dashboard page renders, once a visitor submits valid credentials, and displays every tweet.
- A user may tweet _and_ retweet any tweet, and the visitor's page will display retweets along with their original tweets.
- Your app. demonstrates some level of resilience or fault tolerance by either fetching a resource from IPFS, and then sending it along with a response to a client, or by having IPFS serve hypermedia, itself. Feel free to get creative here, but make sure that you keep your code in a working state.

*Good luck.*
