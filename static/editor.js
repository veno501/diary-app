tinymce.init({
    selector: '#editor',
    auto_focus: 'editor',
    init_instance_callback: function(editor) {
        editor.setContent(initial_content);
        // USE THIS FOR AUTOSAVING - SENDS A POST REQUEST ON EVERY CHANGE
        editor.on('Paste Change input Undo Redo', function(e) {
          $.ajax({
              url: url,
              headers: {'X-CSRFToken': csrf_token},
              data: {'content': editor.getContent(), 'is_autosave_update': true},
              type: "POST",
              dataType: 'json',
              success: function() {
                console.log("Auto saved entry content.")
              }
          });
      })
    },
    width: '100%',
    height: '100%',
    min_height: window.innerHeight - 100,
    resize: false,
    menubar: false,
    plugins: [
      'advlist autolink lists link image charmap print preview anchor',
      'searchreplace visualblocks code fullscreen',
      'insertdatetime media table paste code help wordcount',
      'autoresize',
    ],
    fontsize_formats: '8pt 10pt 12pt 14pt 16pt 18pt 24pt 36pt 48pt',
    toolbar: 'undo redo | fontsizeselect | backcolor | ' +
    'bold italic underline strikethrough | bullist outdent indent |' +
    'image media',
    mobile: {
      toolbar_mode: 'wrap',
    },
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
  });
