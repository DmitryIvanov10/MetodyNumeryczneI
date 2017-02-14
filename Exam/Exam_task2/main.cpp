# include <iostream>
# include <cstdlib>
# include <fstream>
# include <string>

# include <gsl/gsl_spline.h>

using namespace std;

int main ()
{
    const size_t n = 9; // size of initial data arrays
    double x , y; // variables for calculations
    double h = 0.01; // step for iteration

    // initial data
    const double xx[] = {7.99, 8.09, 8.19, 8.7, 9.2, 10.0, 12.0, 15.0, 20.0};
    const double yy[] = {0.0, 0.0000276, 0.04375, 0.169183, 0.469428, 0.94374, 0.998636, 0.999919, 0.999994};

    // initialize and open files for output data
    ofstream spline("spline.txt", ios::out);
    ofstream steffen("spline_steffen.txt", ios::out);
    if (!spline.is_open())
    {
        cout << "Can't open output file" << endl;
        exit(1);
    }
    if (!steffen.is_open())
    {
        cout << "Can't open output file" << endl;
        exit(1);
    }
    spline << " # Re \t CD \n ";
    steffen << " # Re \t CD \n ";

    // initialize data for interpolation calculations
    gsl_interp_accel *acc = gsl_interp_accel_alloc();
    gsl_spline * cspline = gsl_spline_alloc(gsl_interp_cspline, n);
    gsl_spline_init(cspline, xx, yy, n);
    gsl_spline * spline_steffen = gsl_spline_alloc(gsl_interp_steffen, n);
    gsl_spline_init(spline_steffen, xx, yy, n);

    // print results
    cout << "Cubic splines: "<<endl;
    cout << "y (x = 10.8) = " << gsl_spline_eval(cspline, 10.8, acc) << endl;
    cout << "y (x = 13.2) = " << gsl_spline_eval(cspline, 13.2, acc) << endl;
    cout << endl;
    cout << "Steffen splines: "<<endl;
    cout << "y (x = 10.8) = " << gsl_spline_eval(spline_steffen, 10.8, acc) << endl;
    cout << "y (x = 13.2) = " << gsl_spline_eval(spline_steffen, 13.2, acc) << endl;

    // loop to get output data for plots
    x = xx[0];
    while (x <= xx[n-1])
    {
        y = gsl_spline_eval(cspline, x, acc);
        spline << x << " \t " << y << " \n ";

        y = gsl_spline_eval(spline_steffen, x, acc);
        steffen << x << " \t " << y << " \n ";

        x += h;
    }

    spline.close();
    steffen.close();
    gsl_spline_free(cspline);
    gsl_spline_free(spline_steffen);
    gsl_interp_accel_free(acc);

    return 0;
}
