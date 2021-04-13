var editorConfig = {
    selector: '.editor',
    menubar: 'insert',
    inline: false,
    toolbar: 'undo redo | link image',
    //automatic_uploads: true,
    file_picker_types: 'image',
    plugins: 'quickbars image link media',
    mobile: {
        plugins: 'quickbars image link media',
    },
    quickbars_insert_toolbar: false,
    quickbars_selection_toolbar: 'bold italic underline | fontsizeselect',
    height: '60vh',
};

tinymce.init(editorConfig);