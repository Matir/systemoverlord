{% load mezzanine_tags i18n staticfiles %}
$.noConflict();
{% url "static_proxy" as static_proxy_url %}
{% url "fb_browse" as fb_browse_url %}
{% url "admin:index" as admin_index_url %}
{% get_current_language as LANGUAGE_CODE %}
window.__home_link = '<a href="{% url "home" %}">{% trans "View site" %}</a>';
window.__csrf_token = '{{ csrf_token }}';
window.__admin_keywords_submit_url = '{% url "admin_keywords_submit" %}';
window.__filebrowser_url = '{{ fb_browse_url }}';
window.__admin_url = '{{ admin_index_url }}';
var ADMIN_URL = '{{ admin_index_url }}';
window.__static_proxy = '{{ static_proxy_url }}';
window.__admin_media_prefix__ = '{% static "admin" %}/';
window.__grappelli_installed = {{ settings.GRAPPELLI_INSTALLED|lower }};
window.__language_code = '{{ LANGUAGE_CODE }}';

// Format newlines for HTML in the quick blog form, since the content
// is HTML but the form field is plain text.
jQuery(function($) {
    $('#quick-blog-form').submit(function() {
        var field = $('#quick-blog-form #id_content');
        var value = field.attr('value').split('\n\n').join('</p><p>');
        value = '<p>' + value.split('\n').join('<br>') + '</p>';
        field.attr('value', value);
        return true;
    });
});

// Very basic Markdown editor if {{id}} == id
jQuery(document).ready(function () {
  if (typeof Markdown !== "undefined"){
    var converter_id_content = Markdown.getSanitizingConverter();
    var editor_id_content = new Markdown.Editor(converter_id_content, "-id_content");
    editor_id_content.hooks.set("insertImageDialog", browseMediaLibrary);
    editor_id_content.run();
    preview_id_content = '#server-preview-id_content';
    // resize preview along with textarea
    jQuery('#wmd-input-id_content').on('mouseup', function() {
      jQuery(preview_id_content).outerHeight(jQuery('#wmd-input-id_content').outerHeight());
    });

    // scroll preview along with textarea
    jQuery('#wmd-input-id_content').on('scroll', function() {
      jQuery(preview_id_content).scrollTop(
        jQuery('#wmd-input-id_content').scrollTop() / jQuery('#wmd-input-id_content')[0].scrollHeight *
        jQuery(preview_id_content)[0].scrollHeight);
    });

    // server-side preview
    preview = function() {
      jQuery.post('/pagedown/preview/',
          {text:jQuery('#wmd-input-id_content').val()},
          function(data,status) {
            jQuery('#server-preview-id_content').html(data);
          });
    };
    // update the preview on textarea input
    jQuery('#wmd-input-id_content').on('input onpropertychange', jQuery.debounce(250,preview));
    // update the preview on pagedown editor button clicks
    jQuery('#wmd-button-bar-id_content').on('click', preview);
    // initial preview on loading the page
    jQuery(document).ready(preview);
  }
});
