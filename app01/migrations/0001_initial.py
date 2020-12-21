# Generated by Django 3.1.4 on 2020-12-19 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('aid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('normalized_name', models.CharField(max_length=50)),
                ('org', models.CharField(max_length=50)),
                ('n_citation', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=50)),
                ('n_pubs', models.IntegerField(default=0)),
                ('h_index', models.IntegerField(default=0)),
                ('is_recorded', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('manager_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('pid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('venue_name', models.CharField(default='', max_length=50)),
                ('year', models.IntegerField(default=2000)),
                ('n_citation', models.IntegerField(default=0)),
                ('page_start', models.IntegerField(default=0)),
                ('page_end', models.IntegerField(default=0)),
                ('doc_type', models.CharField(default='', max_length=50)),
                ('lan', models.CharField(default='', max_length=50)),
                ('publisher', models.CharField(default='', max_length=50)),
                ('volume', models.IntegerField(default=0)),
                ('issue', models.CharField(default='', max_length=50)),
                ('issn', models.CharField(default='', max_length=50)),
                ('isbn', models.CharField(default='', max_length=50)),
                ('doi', models.CharField(default='', max_length=50)),
                ('pdfURL', models.CharField(default='', max_length=500)),
                ('abstract', models.TextField(default='', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('aid', models.IntegerField(default=-1)),
                ('password', models.CharField(default='a12345678', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('intro', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('vid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=500)),
                ('normalized_name', models.CharField(max_length=500)),
                ('paper_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.user')),
            ],
        ),
        migrations.CreateModel(
            name='SystemMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('type_node', models.IntegerField(default=-1)),
                ('user', models.ForeignKey(on_delete=models.Model, to='app01.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper', to='app01.paper')),
                ('referenced_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referenced_paper', to='app01.paper')),
            ],
        ),
        migrations.CreateModel(
            name='PaperURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.paper')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.venue'),
        ),
        migrations.CreateModel(
            name='KeyWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.paper')),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.author')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.author')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.user')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fos', models.CharField(max_length=100)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.paper')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.paper')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.user')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.author')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorOfPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.author')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.paper')),
            ],
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['aid'], name='aid'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['is_recorded'], name='is_recorded'),
        ),
        migrations.AddIndex(
            model_name='paper',
            index=models.Index(fields=['pid'], name='pid'),
        ),
        migrations.AddIndex(
            model_name='paper',
            index=models.Index(fields=['title'], name='title'),
        ),
    ]
