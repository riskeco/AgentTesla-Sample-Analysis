
all: dn-extractor.exe config.exe decrypt-all.exe

dn-extractor.exe: dn-extractor.cs
	mcs -out:dn-extractor.exe dn-extractor.cs /reference:System.Drawing.dll

config.exe: config.cs
	mcs -out:config.exe config.cs

decrypt-all.exe: decrypt-all.cs
	mcs -out:decrypt-all.exe decrypt-all.cs
