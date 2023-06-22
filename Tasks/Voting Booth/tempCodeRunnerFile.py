draw a new chart every time the results tab is opened (call show_results)
notebook.bind('<<NotebookTabChanged>>',
              lambda event: show_results() if event.widget.tab('current')['text'] == 'Results' else None)

root.mainloop()