SELECT DISTINCT tweets.pk, tweets.users_pk, tweets.username, tweets.content, tweets.time
FROM tweets
INNER JOIN users_followed
ON tweets.users_pk= 1;



-- row_place.append(row["pk"]) 
-- row_place.append(row["users_pk"])
-- row_place.append(row["username"])
-- row_place.append(row["content"]) 
-- row_place.append(row["time"]) 