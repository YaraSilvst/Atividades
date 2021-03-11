#include <stdio.h>

int op;
int controlador = 0;
#define Vet_Pessoa 10;

typedef struct Pessoa
{
    char nome[30];
    int telefone[15];
    int codigo;
    char email;
    char aniversario[8];
    char anotacoes[120];
} Pessoa;

struct Pessoa Pessoa[10];

void menu()
{
    printf(" --------------------- \n");
    printf("          AGENDA       \n");
    printf(" --------------------- \n");
    printf(" 1 - Cadastrar         \n");
    printf(" 2 - Listar            \n");
    printf(" 3 - Alterar           \n");
    printf(" 4 - Excluir           \n");
    printf(" 5 - Sair              \n");
    printf(" --------------------- \n");
}

void cadastro()
{
    if (controlador < 10)
    {
        do
        {
            printf("\nCodigo: ");
            scanf("%i", &Pessoa[controlador].codigo);
        }

        while (Pessoa[controlador].codigo <= 0);

        printf("\nNome: ");
        fgets(Pessoa[controlador].nome, 30, stdin);

        printf("\nTelefone: ");
        scanf("%i", &Pessoa[controlador].telefone);
        getchar();

        printf("\nEmail: ");
        fgets(Pessoa[controlador].email, 30, stdin);

        printf("\nAniversario: ");
        fgets(Pessoa[controlador].aniversario, 30, stdin);

        printf("\nAnotacoes: ");
        fgets(Pessoa[controlador].anotacoes, 30, stdin);

        controlador++;
    }

    else
    {
        printf("Agenda Lotada");
    }

    void listar()
    {
        if (controlador > 0)
        {
            for (int i = 0; i < controlador; i++)
            {
                printf("%d\n", Pessoa[i].codigo);
                printf("%s\n", Pessoa[i].nome);
                printf("%s\n", Pessoa[i].telefone);
                printf("%s\n", Pessoa[i].email);
                printf("%s\n", Pessoa[i].aniversario);
                printf("%s\n", Pessoa[i].anotacoes);
            }
        }

        else
        {
            print("Sem Cadastro");
        }
    }

    int main()
    {
        int op = 10;

        while (op != 0)
        {
            menu();
            printf("");
            scanf("%i", &op);
            getchar();

            if (op == 6)
            {
                printf("Codigo Encerrado");

                op = 0;
            }

            else if (op == 1)
            {
                cadastro();
            }

            else if (op == 2)
            {
                listar();
            }

            else if (op == 3)
            {
                print("Em andamento");
            }

            else if (op == 4)
            {
                print("Em andamento");
            }

            else
            {
                printf("Opcao Invalida");
            }
        }
    
    }