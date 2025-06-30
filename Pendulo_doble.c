#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define h 0.001
#define g 9.81

typedef struct {
    double thetha,phi;
    double thethap,phip;
} cuerpos;

//hago las funciones para evaluar las derivadas a apartir de f
double ftheta(double thetap)
{
    return thetap;
}

double fphi(double phip)
{
    return phip;
}

double fthethap(double thetha, double phi, double thethap, double phip)
{
    return (g*sin(phi)*cos(-phi+thetha) - 2*g*sin(thetha) - pow(phip, 2)*cos(-phi+thetha)*sin(-phi+thetha) - pow(phip, 2)*sin(-phi + thetha))/(2 - pow(cos(-phi+thetha), 2));
}

double fphip(double thetha, double phi, double thethap, double phip)
{
    return (g*sin(thetha)*cos(-phi+thetha) - g*sin(phi) + 0.5*pow(phip, 2)*cos(-phi+thetha)*sin(-phi+thetha) + pow(phip, 2)*sin(-phi+thetha))/(1 - 0.5*pow(cos(-phi+thetha), 2));
}


void runge_kuttap(cuerpos *cuerpo, FILE *file)
{
    double k[4][4];  

    // Evaluo k1
    k[0][0] = h * ftheta(cuerpo->thethap);
    k[1][0] = h * fphi(cuerpo->phip);
    k[2][0] = h * fthethap(cuerpo->thetha, cuerpo->phi, cuerpo->thethap, cuerpo->phip);
    k[3][0] = h * fphip(cuerpo->thetha, cuerpo->phi, cuerpo->thethap, cuerpo->phip);

    // Evaluo k2
    k[0][1] = h * ftheta(cuerpo->thethap + k[2][0]/2);
    k[1][1] = h * fphi(cuerpo->phip + k[3][0]/2);
    k[2][1] = h * fthethap(cuerpo->thetha + k[0][0]/2, cuerpo->phi + k[1][0]/2, cuerpo->thethap + k[2][0]/2, cuerpo->phip + k[3][0]/2);
    k[3][1] = h * fphip(cuerpo->thetha + k[0][0]/2, cuerpo->phi + k[1][0]/2, cuerpo->thethap + k[2][0]/2, cuerpo->phip + k[3][0]/2);

    // Evaluo k3
    k[0][2] = h * ftheta(cuerpo->thethap + k[2][1]/2);
    k[1][2] = h * fphi(cuerpo->phip + k[3][1]/2);
    k[2][2] = h * fthethap(cuerpo->thetha + k[0][1]/2, cuerpo->phi + k[1][1]/2, cuerpo->thethap + k[2][1]/2, cuerpo->phip + k[3][1]/2);
    k[3][2] = h * fphip(cuerpo->thetha + k[0][1]/2, cuerpo->phi + k[1][1]/2, cuerpo->thethap + k[2][1]/2, cuerpo->phip + k[3][1]/2);

    // Evaluo k4
    k[0][3] = h * ftheta(cuerpo->thethap + k[2][2]);
    k[1][3] = h * fphi(cuerpo->phip + k[3][2]);
    k[2][3] = h * fthethap(cuerpo->thetha + k[0][2], cuerpo->phi + k[1][2], cuerpo->thethap + k[2][2], cuerpo->phip + k[3][2]);
    k[3][3] = h * fphip(cuerpo->thetha + k[0][2], cuerpo->phi + k[1][2], cuerpo->thethap + k[2][2], cuerpo->phip + k[3][2]);

    // Actualizo las variables 
    cuerpo->thetha   += (k[0][0] + 2*k[0][1] + 2*k[0][2] + k[0][3]) / 6;
    cuerpo->phi      += (k[1][0] + 2*k[1][1] + 2*k[1][2] + k[1][3]) / 6;
    cuerpo->thethap  += (k[2][0] + 2*k[2][1] + 2*k[2][2] + k[2][3]) / 6;
    cuerpo->phip     += (k[3][0] + 2*k[3][1] + 2*k[3][2] + k[3][3]) / 6;

    // Guardo los resultados
    fprintf(file, "%lf, %lf, %lf, %lf\n", cuerpo->thetha, cuerpo->phi, cuerpo->thethap, cuerpo->phip);
}



int main (void)
{
    FILE *file, *file2, *file3, *file4;
    file = fopen("Pendulo_doble.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    file2 = fopen("Mapa_Poincare_thetha_phi.txt", "w");
    if (file2 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    file3 = fopen("Mapa_Poincare_thethap_thetha.txt", "w");
    if (file3 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    file4 = fopen("Mapa_Poincare_phi_phip.txt", "w");
    if (file4 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    //Defino las variables
    cuerpos cuerpo;
    double E;
    E=1;
    cuerpo.thetha=0.05;
    cuerpo.phi=0.75;
    cuerpo.thethap=sqrt(2*(E+9.8*(2*cos(cuerpo.thetha)+cos(cuerpo.phi))-3*9.8));
    //cuerpo.thethap=0;
    cuerpo.phip=0.0;
    

    //Voy a guardar los resultados en un archivo
    fprintf(file, "%lf, %lf, %lf, %lf\n", cuerpo.thetha, cuerpo.phi, cuerpo.thethap, cuerpo.phip);

    //Voy a hacer el ciclo para calcular la trayectoria
    for(double i=0; i<100; i += h)
    {
        runge_kuttap(&cuerpo, file);

        //Para calcular el mapa de Poincaré theta-phi
        
         fprintf(file2,"%lf, %lf\n", cuerpo.thetha, cuerpo.phi );
         

        //Para calcular el mapa de Poincaré thetapunto-theta
        
         fprintf(file3,"%lf, %lf\n", cuerpo.thethap, cuerpo.thetha );
        

        //Para calcular el mapa de Poincaré phipunto-phi
       
         fprintf(file4,"%lf, %lf\n", cuerpo.phi, cuerpo.phip );
        
    }

    
   


    fclose(file);
    fclose(file2);
    fclose(file3);
    fclose(file4);
    return 0;
}