#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QMessageBox>
#include <QProcess>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->pushButton, &QPushButton::clicked, this, &MainWindow::on_pushButton_clicked);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QString folderPath=QFileDialog::getExistingDirectory(
        this,
        tr("Open Folder"),
        "C://"
    );

    if (!folderPath.isEmpty()) {
        QMessageBox::information(this, tr("Folder Path"), folderPath);
        compressFolder(folderPath);

    }
}

void MainWindow::compressFolder(const QString &folderPath)
{
    // Check if the Python script exists
    QString pythonScript = "compress.py"; // Le chemin vers le script Python
    if (!QFile::exists(pythonScript)) {
        QMessageBox::critical(this, tr("Script Not Found"), tr("The Python script '%1' was not found.").arg(pythonScript));
        return;
    }

    // Exécuter le script Python pour compresser le fichier
    QProcess process;
    QString program = "python"; // Le programme Python
    QStringList arguments; // Les arguments pour le script Python
    arguments << pythonScript << folderPath; // Ajouter les arguments pour le script Python

    process.start(program, arguments); // Démarrer le processus

    // Attendre que le processus se termine (bloquant)
    process.waitForFinished(-1);

    // Vérifier le code de sortie du processus
    if (process.exitCode() == 0) {
        QMessageBox::information(this, tr("Compression Successful"), tr("File compressed successfully"));
    } 
    else {
        QMessageBox::warning(this, tr("Compression Failed"), tr("Failed to compress file: %1").arg(folderPath));
    }
}

void MainWindow::on_pushButton_2_clicked()
{
    QString filename=QFileDialog::getOpenFileName(
        this,
        tr("Open File"),
        "C://",
        "All files (*.*);; Text File (*.txt);;Music file(*.mp3);; Image File(*.png)"
        );
    QMessageBox::information(this, tr("File Name"), filename);
}

