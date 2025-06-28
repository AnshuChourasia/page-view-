# This entrypoint file to be used in development. Start by reading README.md
# main.py

from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Draw Line Plot
print("Generating Line Plot...")
fig1 = draw_line_plot()
fig1.savefig('line_plot.png')
print("line_plot.png saved")

# Draw Bar Plot
print("Generating Bar Plot...")
fig2 = draw_bar_plot()
fig2.savefig('bar_plot.png')
print("bar_plot.png saved")

# Draw Box Plot
print("Generating Box Plot...")
fig3 = draw_box_plot()
fig3.savefig('box_plot.png')
print("box_plot.png saved")


# Run unit tests automatically
#main(module='test_module', exit=False)