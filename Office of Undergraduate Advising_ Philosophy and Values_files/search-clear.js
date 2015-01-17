$(document).ready(function(focusClass) {
    $('#search_box').focus(function() {

    // clear value if current value is the default
    if($(this).val() == this.defaultValue) { $(this).val(""); }

    // if focusClass is set, add the class
    if(focusClass) { $(this).addClass(focusClass); }}).blur(function() {
    // restore to the default value if current value is empty
    if($(this).val() == "") { $(this).val(this.defaultValue); }

    });
});



