// window.onload = iniiAll;

// let saveBookButton;
// function iniiAll() {
//     saveBookButton = document.getElementById('save_book');
//     saveBookButton.onclick = saveBook;
// }

// function saveBook() {

//     let name = document.getElementById("book_name").value;
//     let prize = document.getElementById("book_prize").value;
//     let pages = document.getElementById("book_pages").value;

//     let url = '/save_book?name=' + name + '&prize=' + prize + '&pages=' + pages;
//     //alert(url);

//     var req = new XMLHttpRequest();
//     req.onreadystatechange = function () {
//         if (this.readyState == 4 && this.status == 200) {

//         }
//     };
//     req.open("GET", url, true);
//     req.send();
// }