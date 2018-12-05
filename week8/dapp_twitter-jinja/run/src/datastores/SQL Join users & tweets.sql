SELECT tweets.pk, tweets.users_pk, tweets.username, tweets.content, tweets.time
FROM tweets
JOIN users_followed
ON users_followed.users_pk = 2
JOIN tweets
ON users_followed.followed_pk =  tweets.users.pk;




-- row_place.append(row["pk"]) 
-- row_place.append(row["users_pk"])
-- row_place.append(row["username"])
-- row_place.append(row["content"]) 
-- row_place.append(row["time"]) 