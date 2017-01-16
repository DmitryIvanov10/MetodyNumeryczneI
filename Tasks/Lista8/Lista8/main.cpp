# include <iostream>
# include <cstdlib>
# include <fstream>
# include <string>

# include <gsl/gsl_errno.h>
# include <gsl/gsl_interp.h>
# include <gsl/gsl_spline.h>

using namespace std;

int main ()
{
    size_t n = 6;
    double x , y;
    double Re [] = {0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0};
    double CD [] = {103.0, 13.9, 2.72, 0.8, 0.401, 0.433};
    ofstream polynom("task2_polynom.txt", ios::out);
    ofstream spline("task2_spline.txt", ios::out);
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
    polynom << " # Re \t CD \n ";
    spline << " # Re \t CD \n ";
    gsl_interp_accel * acc = gsl_interp_accel_alloc();
    gsl_interp * poly = gsl_interp_alloc(gsl_interp_polynomial, n);
    gsl_interp_init(poly, Re, CD, n);
    gsl_spline * spl = gsl_spline_alloc(gsl_interp_cspline, n);
    gsl_spline_init(spl, Re, CD, n);

    for (int i = 0; i <= 20000; i+=10)
    {
        x = Re[0] + i;
        y = gsl_interp_eval(poly, Re, CD, x, acc);
        polynom << x << " \t " << y << " \n ";

        y = gsl_spline_eval(spl, x, acc);
        spline << x << " \t " << y << " \n ";
    }
    polynom.close();
    gsl_interp_free(poly);
    gsl_spline_free(spl);
    gsl_interp_accel_free(acc);
}
