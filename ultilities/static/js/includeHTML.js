function includeHTML() {
  var z, i, element, file, xhttp;

  /*loop through a collection of all HTML elements:*/
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    element = z[i];

    /*search for elements with a certain atrribute:*/
    file = element.getAttribute("include-html");

    if (file) {
      /*make an HTTP request using the attribute value as the file name:*/
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {element.innerHTML = this.responseText;}
          if (this.status == 404) {element.innerHTML = "Page not found.";}
          
          /*remove the attribute, and call this function once more:*/
          element.removeAttribute("include-html");
          includeHTML();
        }
      }      

      xhttp.open("GET", file, true);
      xhttp.send();
      
      return;
    }
  }
};