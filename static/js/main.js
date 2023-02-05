jQuery.fn.center = function () {
    this.css('position', 'absolute');
    this.css('top', '150px');
    this.css('left', '200px');
    return this;
};

jQuery.fn.ajaxMask = function () {
    this.children('*').fadeTo(0, 0.2);
    this.prepend($('<img/>').attr('src', 'static/img/ajax.gif'));
    this.children('img').center();
    return this;
};

