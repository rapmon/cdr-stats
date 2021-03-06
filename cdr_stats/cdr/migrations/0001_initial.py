# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Company'
        db.create_table('cdr_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=400, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('cdr', ['Company'])

        # Adding model 'UserProfile'
        db.create_table('cdr_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('accountcode', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cdr.Company'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('cdr', ['UserProfile'])

        # Adding model 'CDR'
        db.create_table('cdr', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('src', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('dst', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('calldate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('clid', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('dcontext', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('dstchannel', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('lastapp', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('lastdata', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('billsec', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('disposition', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('amaflags', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('accountcode', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('uniqueid', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('userfield', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
        ))
        db.send_create_signal('cdr', ['CDR'])


    def backwards(self, orm):
        
        # Deleting model 'Company'
        db.delete_table('cdr_company')

        # Deleting model 'UserProfile'
        db.delete_table('cdr_userprofile')

        # Deleting model 'CDR'
        db.delete_table('cdr')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cdr.cdr': {
            'Meta': {'object_name': 'CDR', 'db_table': "'cdr'"},
            'accountcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'amaflags': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'billsec': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'calldate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'clid': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'dcontext': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'disposition': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'dst': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'dstchannel': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastapp': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'lastdata': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'src': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'uniqueid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'userfield': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'cdr.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'cdr.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'accountcode': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cdr.Company']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cdr']
