#!/bin/bash
asciidoctor-pdf -a source-highlighter=rouge -a rouge-style=colorful commandes-compilation.adoc
asciidoctor -a source-highlighter=rouge -a rouge-style=colorful QRH_BD.adoc
asciidoctor-pdf -a source-highlighter=rouge -a rouge-style=colorful QRH_BD.adoc
asciidoctor-epub3 -a source-highlighter=rouge -a rouge-style=colorful QRH_BD.adoc
