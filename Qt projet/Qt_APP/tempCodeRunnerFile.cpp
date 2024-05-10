if (process.exitCode() == 0) {
        QMessageBox::information(this, tr("Compression Successful"), tr("File compressed successfully"));
    } else {
        QMessageBox::warning(this, tr("Compression Failed"), tr("Failed to compress file: %1").arg(folderPath));
    }