function followUser() {
  user_name = document.querySelector("#user_name").innerHTML
  console.log("test");

  fetch('/following', {
    method: "PUT",
    body: JSON.stringify({
      to_follow: user_name,
    })
  })
  .then(response => response.json())
  .then(response => {
    const follow_txt = response["follow_status"]
    const follower_count = response["follow_count"]
    console.log(follow_txt)
    const follow_button = document.querySelector("#follow-button")
    const follow_count = document.querySelector("#follow-count")
    follow_count.innerHTML = `Followers: ${follower_count}`
    follow_button.innerHTML = follow_txt
    console.log(follow_button)
  });
}

function likePost(id) {
  const like_id = id.replace("like","")

  fetch('/likepost',  {
    method: 'PUT',
    body: JSON.stringify({
      id: like_id,
    })
  })
  .then(response => response.json())
  .then(response => {
    const like_total = response["count"]
    const like_html = document.querySelector(`#${id}`)
    like_html.innerHTML = `❤ ${like_total}`
  } );
}

function editPost(id) {
  id_no = id.replace("edit","")

  // elements
  edit_button = document.querySelector(`#${id}`)
  content = document.querySelector(`#content${id_no}`)
  edit_box = document.querySelector(`#editbox${id_no}`)

  // hide/show content/edit box
  if (edit_button.innerHTML === "EDIT") {
    edit_box.hidden = false;
    edit_button.innerHTML = "CANCEL";
  }
  else {
    edit_box.hidden = true;
    edit_button.innerHTML = "EDIT"
  }

}

function submitEdit(id) {
  new_content = document.querySelector(`#newcontent${id}`).value
  console.log(new_content)
  fetch("/editpost", {
    method: "PUT",
    body: JSON.stringify({
      "post_id": id,
      "new_content": new_content
    })
  })
  .then(response => response.json())
  .then(response => {
    console.log(response["new_content"])
    content = document.querySelector(`#content${id}`)
    edit_button = document.querySelector(`#edit${id}`)
    edit_box = document.querySelector(`#editbox${id}`)
    // return to orginal
    if (edit_button.innerHTML === "EDIT") {
      edit_box.hidden = false;
      edit_button.innerHTML = "CANCEL";
    }
    else {
      edit_box.hidden = true;
      edit_button.innerHTML = "EDIT"
    }
    content.innerHTML = response["new_content"]
    new_content.innerHTML = response["new_content"]
  
  })

}
  
  