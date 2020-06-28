FOR GET DATA in LIST EXAMPLE
curl http://127.0.0.1:8000/posts/


=====================================================
FOR POST DATA MEANS  INSERT DATA in TABLE
curl -X PUT http://127.0.0.1:8000/posts/1/ -d post_title="Demo Post Updated" -d post_descripti
on="Demo Description Updated"

=========================================================
FOR UPDATE into TABLE BY ID
curl -X PUT http://127.0.0.1:8000/posts/1/ -d post_title="Demo Post Updated" -d post_descripti
on="Demo Description Updated"


=========================================================
FOR DELETE DATA DATA BY ID
curl -X DELETE  http://127.0.0.1:8000/posts/1/

=========================================================
FOR SINGLE POST FETCH BY ID
curl http://127.0.0.1:8000/posts/1/





