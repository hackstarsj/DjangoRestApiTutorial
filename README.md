FOR GET DATA in LIST EXAMPLE
<br>
<br>
curl http://127.0.0.1:8000/posts/


<br>
=====================================================
<br>
FOR POST DATA MEANS  INSERT DATA in TABLE
<br>
<br>
curl -X PUT http://127.0.0.1:8000/posts/1/ -d post_title="Demo Post Updated" -d post_descripti
on="Demo Description Updated"
<br>
<br>
=========================================================
<br>
<br>
FOR UPDATE into TABLE BY ID
<br>
<br>
curl -X PUT http://127.0.0.1:8000/posts/1/ -d post_title="Demo Post Updated" -d post_descripti
on="Demo Description Updated"
<br>

<br>
=========================================================
<br>
FOR DELETE DATA DATA BY ID
<br>
<br>
curl -X DELETE  http://127.0.0.1:8000/posts/1/
<br>
<br>
=========================================================
<br>
<br>
FOR SINGLE POST FETCH BY ID
<br>
curl http://127.0.0.1:8000/posts/1/
<br>
<br>

=================================================
<br>
<h2>For Alternate Method for Seprate POST,GET,PUT</h2>

FOR GET DATA in LIST EXAMPLE
<br>
<br>
curl http://127.0.0.1:8000/posts_2/


<br>
=====================================================
<br>
FOR POST DATA MEANS  INSERT DATA in TABLE
<br>
<br>
curl -X PUT http://127.0.0.1:8000/posts_2/1/ -d post_title="Demo Post Updated" -d post_descripti
on="Demo Description Updated"
<br>
<br>
=========================================================
<br>
<br>
FOR UPDATE into TABLE BY ID
<br>
<br>
curl -X PUT http://127.0.0.1:8000/posts_2/1/ -d post_title="Demo Post Updated" -d post_descripti
on="Demo Description Updated"
<br>

<br>
=========================================================
<br>
FOR DELETE DATA DATA BY ID
<br>
<br>
curl -X DELETE  http://127.0.0.1:8000/posts_2/1/
<br>
<br>
=========================================================
<br>
<br>
FOR SINGLE POST FETCH BY ID
<br>
curl http://127.0.0.1:8000/posts_2/1/
<br>
<br>

=================================================