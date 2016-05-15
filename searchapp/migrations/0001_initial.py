# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import searchapp.custom


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryName', models.CharField(max_length=60, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=120, verbose_name=b'Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title of the paper')),
                ('document', models.TextField(blank=True)),
                ('source', models.TextField(default=b'ACM Digital Library', blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('publishedYear', models.IntegerField(default=2015, verbose_name=b'year')),
                ('timeInsertion', models.DateTimeField(auto_now=True, verbose_name=b'Added on')),
                ('author', models.ManyToManyField(to='searchapp.Author', blank=True)),
                ('category', models.ManyToManyField(to='searchapp.Category', blank=True)),
                ('keywords', models.ManyToManyField(to='searchapp.Keyword', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaperUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(help_text=b'Browse a file', upload_to=searchapp.custom.wrapper, null=True, verbose_name=b'Upload File')),
                ('identify', models.CharField(default=b'Uploaded Paper', max_length=60, verbose_name=b'Title')),
                ('publishedYear', models.IntegerField(default=2015, verbose_name=b'year', choices=[(1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1200, verbose_name=b'References')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sourceName', models.CharField(max_length=60, verbose_name=b'Source')),
            ],
        ),
        migrations.AddField(
            model_name='paperupload',
            name='source',
            field=models.ForeignKey(blank=True, to='searchapp.Source', max_length=60),
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_upload',
            field=models.ForeignKey(blank=True, to='searchapp.PaperUpload', null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='references',
            field=models.ManyToManyField(to='searchapp.Reference', blank=True),
        ),
    ]
