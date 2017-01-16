# include <iostream>
# include <cstdlib>
# include <fstream>
# include <string>

# include <gsl/gsl_errno.h>
//# include <gsl/gsl_interp.h>
# include <gsl/gsl_spline.h>

using namespace std;

int main ()
{
    const size_t n = 6;
    double x , y;
    const double Re [] = {0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0};
    const double CD [] = {103.0, 13.9, 2.72, 0.8, 0.401, 0.433};
    ofstream polynom("task2_polynom.txt", ios::out);
    ofstream spline("task2_spline.txt", ios::out);
    ofstream steffen("task2_spline_steffen.txt", ios::out);
    if (!polynom.is_open())
    {
        cout << "Can't open output file" << endl;
        exit(1);
    }
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
    polynom << " # Re \t CD \n ";
    spline << " # Re \t CD \n ";
    steffen << " # Re \t CD \n ";
    gsl_interp_accel *acc = gsl_interp_accel_alloc();
    gsl_interp * poly = gsl_interp_alloc(gsl_interp_polynomial, n);
    gsl_interp_init(poly, Re, CD, n);
    gsl_spline * spl = gsl_spline_alloc(gsl_interp_cspline, n);
    gsl_spline_init(spl, Re, CD, n);
    gsl_spline * spline_steffen = gsl_spline_alloc(gsl_interp_steffen, n);
    gsl_spline_init(spline_steffen, Re, CD, n);

    cout << "CD (Re = 5.5) = " << gsl_spline_eval(spline_steffen, 5.5, acc) << endl;
    cout << "CD (Re = 5000) = " << gsl_spline_eval(spline_steffen, 5000, acc) << endl;

    for (int i = 0; i <= 20000; i+=10)
    {
        x = Re[0] + i;
        y = gsl_interp_eval(poly, Re, CD, x, acc);
        polynom << x << " \t " << y << " \n ";

        y = gsl_spline_eval(spl, x, acc);
        spline << x << " \t " << y << " \n ";

        y = gsl_spline_eval(spline_steffen, x, acc);
        steffen << x << " \t " << y << " \n ";
    }
    polynom.close();
    spline.close();
    steffen.close();
    gsl_interp_free(poly);
    gsl_spline_free(spl);
    gsl_spline_free(spline_steffen);
    gsl_interp_accel_free(acc);
    return 0;
}
