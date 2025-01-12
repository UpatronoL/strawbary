set terminal png size 800,600
set output 'temperature_plot.png'
set title 'Hourly Average Temperature'
set xlabel 'Hour'
set ylabel 'Temperature (°C)'
set grid
plot 'temperature_data.dat' using 1:2 title 'Air Temperature', 1:3 title 'Ground Temperature' with lines title 'Data'
