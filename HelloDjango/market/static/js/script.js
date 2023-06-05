
function redirect_from(url) {
   window.location.href = "https://" + url;
}
function redirect(url) {
   window.location.href = url;
}

function login_error(url) {
   redirect(url);
}

let color = 0;

function swap_color() {

   if (color++ % 2 == 0) {
      document.documentElement.style
         .setProperty('--main-color', 'white');
      document.documentElement.style
         .setProperty('--sub-color', 'black');
   } else {
      document.documentElement.style
         .setProperty('--main-color', 'black');
      document.documentElement.style
         .setProperty('--sub-color', 'white');
   }

}