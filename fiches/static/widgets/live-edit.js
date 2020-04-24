// Start editing the component
function edit(root) {
  const controls = root.find('.edit-controls')
  const content_holder = root.find('.edit-content')
  const pretty_content_holder = root.find('.pretty-content')
  const has_pretty_content_holder = pretty_content_holder.length > 0
  const endpoint = root.data('endpoint')

  // Pull content from div
  const content = content_holder
        .html()
        .replace(/<br>/g, '\n')
        .trim()

  // Replace by textarea
  const textarea = $('<textarea>')
        .val(content)
        .on('input', _ => enable_save())
  content_holder.html(textarea)

  // Replace the controls
  const old_controls = controls.html()
  const new_controls = $(
    `<button class="btn-default cancel">Annuler</button>
       <button class="btn-default save" disabled>Enregistrer</button>`)
  $(new_controls[0])
    .on('click', _ => restore())
  const save_button = $(new_controls[2])
        .on('click', _ => save())
  controls.html(new_controls)

  // Hide pretty contents if they exist
  if (has_pretty_content_holder)
  {
    pretty_content_holder.hide()
    content_holder.show()
  }

  // Enable the save button
  function enable_save() {
    save_button.prop('disabled', false)
  }

  // Send the text content of EL to the server for saving.
  function save() {
    const newcontent = textarea.val().trim()
    if (has_pretty_content_holder)
      content_holder.hide()

    $.post(endpoint, {content: newcontent})
      .fail(_ => {
	  controls.html(new_controls)
	  content_holder.html(textarea)
          textarea.addClass('invalid')
          // TODO: on error, include error message
      })
      .done(answer => {
	if (has_pretty_content_holder)
	  pretty_content_holder.html(answer)
	restore(newcontent)
      })
  }

  // Restore controls and content
  function restore(newcontent = content) {
    controls.html(old_controls)
    content_holder.html(newcontent.replace(/\n/g, '<br>'))

    if (has_pretty_content_holder)
    {
      pretty_content_holder.show()
      content_holder.hide()
    }
  }
}
