#!/bin/bash
all :
	asciidoctor-pdf -a source-highlighter=rouge -a rouge-style=github commandes-compilation.adoc
	asciidoctor -a source-highlighter=rouge -a rouge-style=github QRH_BD.adoc
	asciidoctor-pdf -a source-highlighter=rouge -a rouge-style=github QRH_BD.adoc
	asciidoctor-epub3 -a source-highlighter=rouge -a rouge-style=github QRH_BD.adoc
