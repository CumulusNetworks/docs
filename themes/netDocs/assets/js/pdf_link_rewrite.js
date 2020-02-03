function replace_url() {
    var elems = document.getElementsByTagName("a");
    for (var i = 0; i < elems.length; i++) {
        path = elems[i]["href"];
        path_parts = path.split("/");
        if(path_parts[3] != "{{.Section}}"){
          continue
        }
        if(path_parts[path_parts.length - 1] == ""){
          elems[i]["href"] = "#" + path_parts[path_parts.length - 2];
        }
        else { 
          if(path_parts[path_parts.length - 1].charAt(0) == "#"){
            elems[i]["href"] = path_parts[path_parts.length - 1]
          }
          else{
            elems[i]["href"] = "#" + path_parts[path_parts.length - 1]
          }
        }
        
      }
}

window.onload = function() {
  replace_url();
}