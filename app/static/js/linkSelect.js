//This script makes the current link bold

$(document).ready(function(){
  $(".toplinks a").each(function(){
    if($(this).prop('href') == window.location.href){
      $(this).addClass('current');
    }
  });
});
