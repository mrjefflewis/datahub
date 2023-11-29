# Inlined from /metadata-ingestion/examples/library/dataset_schema.py
# Imports for urn construction utility methods
from datahub.emitter.mce_builder import make_data_platform_urn, make_dataset_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter


from typing import List

import datahub.emitter.mce_builder as builder

from datahub.metadata.com.linkedin.pegasus2avro.datajob import DataJobInputOutputClass
from datahub.metadata.schema_classes import DataFlowInfoClass

# Imports for metadata model classes
from datahub.metadata.schema_classes import (
    AuditStampClass,
    DateTypeClass,
    OtherSchemaClass,
    SchemaFieldClass,
    SchemaFieldDataTypeClass,
    SchemaMetadataClass,
    StringTypeClass,
    NumberTypeClass,
)

def createBronzeTables():
    """ 
    "example schema for a social network database. 
    users can check into locations they visit, 
    they can have friends, 
    they can post into a newsfeed, 
    they view pages, 
    there are advertisements served in the page views, 
    and it needs be measured if they click on the page"


    1. Users Table:
        * user_id (primary key)
        * username
        * password
        * email
        * profile_picture
    2. Locations Table:
        * location_id (primary key)
        * name
        * address
        * city
        * state
    3. Checkins Table:
        * checkin_id (primary key)
        * user_id (foreign key referencing Users table)
        * location_id (foreign key referencing Locations table)
        * date_checked_in
    4. Friends Table:
        * friend_id (primary key)
        * user_id (foreign key referencing Users table)
        * friend_user_id (foreign key referencing Users table)
    5. Newsfeed Table:
        * newsfeed_id (primary key)
        * post_id (foreign key referencing Posts table)
        * user_id (foreign key referencing Users table)
    6. Posts Table:
        * post_id (primary key)
        * user_id (foreign key referencing Users table)
        * content
        * timestamp
    7. Advertisements Table:
        * advertisement_id (primary key)
        * page_id (foreign key referencing Pages table)
        * advertiser_id (foreign key referencing Users table)
    8. Page Views Table:
        * page_view_id (primary key)
        * page_id (foreign key referencing Pages table)
        * user_id (foreign key referencing Users table)
        * timestamp
    9. Clicks Table:
        * click_id (primary key)
        * page_view_id (foreign key referencing Page Views table)
        * timestamp """


    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.users", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="users",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="username",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Username of the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="password",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Password of the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="email",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Email of the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="profile_picture",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Profile picture of the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)


    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.locations", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="locations",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="location_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="name",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Name of the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="address",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Address of the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="city",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="City of the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="state",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="State of the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="country",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(100)",
                    description="Country of the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="zipcode",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Zipcode of the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.checkins", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="checkins",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="checkin_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the checkin",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who checked in to the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="location_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Location that the user checked in to",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="date_checked_in",
                    type=SchemaFieldDataTypeClass(type=DateTypeClass()),
                    nativeDataType="DATE",
                    description="Date the user checked in to the location",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.friends", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="friends",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="friend_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the friend relationship",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who has a friend",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="friend_user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who is the friend of the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.newsfeed", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="newsfeed",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="newsfeed_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the newsfeed post",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="post_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Post that is in the newsfeed of the user",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User whose newsfeed the post is in",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.posts", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="posts",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="post_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the post",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who made the post",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="content",
                    type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                    nativeDataType="VARCHAR(1000)",
                    description="Content of the post",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),            
                SchemaFieldClass(
                    fieldPath="timestamp",
                    type=SchemaFieldDataTypeClass(type=DateTypeClass()),
                    nativeDataType="TIMESTAMP",
                    description="Timestamp of when the post was made",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.advertisements", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="advertisements",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="advertisement_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the advertisement served in the page view",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="page_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Page that the advertisement was served in the page view of",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="advertiser_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who is the advertiser of the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),            
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.page_views", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="page_views",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="page_view_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="page_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Page that the user viewed and was served advertisements in the page view of",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who viewed the page and was served advertisements in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),            
                SchemaFieldClass(
                    fieldPath="timestamp",
                    type=SchemaFieldDataTypeClass(type=DateTypeClass()),
                    nativeDataType="TIMESTAMP",
                    description="Timestamp of when the user viewed the page and was served advertisements in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.clicks", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="clicks",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),
            fields=[
                SchemaFieldClass(
                    fieldPath="click_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",  # use this to provide the type of the field in the source system's vernacular
                    description="Unique identifier for the click of the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="page_view_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Page view that the user clicked on the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),            
                SchemaFieldClass(
                    fieldPath="timestamp",
                    type=SchemaFieldDataTypeClass(type=DateTypeClass()),
                    nativeDataType="TIMESTAMP",
                    description="Timestamp of when the user clicked on the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

def createSilverTables():
    #show MetadataChangeProposalWrapper for a dataset representing the join of advertisements, users, views and clicks
    event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
        entityUrn=make_dataset_urn(platform="hive", name="social_db.advertisements_users_views_clicks", env="PROD"),
        aspect=SchemaMetadataClass(
            schemaName="advertisements_users_views_clicks",  # not used
            platform=make_data_platform_urn("hive"),  # important <- platform must be an urn
            version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
            hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
            platformSchema=OtherSchemaClass(rawSchema="__insert raw schema here__"),
            lastModified=AuditStampClass(
                time=1640692800000, actor="urn:li:corpuser:ingestion"
            ),        
            fields=[
                SchemaFieldClass(
                    fieldPath="advertisement_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Unique identifier for the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),            
                SchemaFieldClass(
                    fieldPath="page_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="Page that the advertisement was served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),                
                ),            
                SchemaFieldClass(
                    fieldPath="advertiser_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who is the advertiser of the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),            
                SchemaFieldClass(
                    fieldPath="user_id",
                    type=SchemaFieldDataTypeClass(type=NumberTypeClass()),
                    nativeDataType="integer",
                    description="User who viewed the page and was served advertisements in the page view of the page and clicked on the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
                SchemaFieldClass(
                    fieldPath="timestamp",
                    type=SchemaFieldDataTypeClass(type=DateTypeClass()),
                    nativeDataType="TIMESTAMP",
                    description="Timestamp of when the user viewed the page and was served advertisements in the page view of the page and clicked on the advertisement served in the page view of the page",
                    lastModified=AuditStampClass(
                        time=1640692800000, actor="urn:li:corpuser:ingestion"
                    ),
                ),
            ],
        ),
    )

    # Create rest emitter
    rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
    rest_emitter.emit(event)

def createJobs():

    # Construct the DataJobInfo aspect with the job -> flow lineage.
    dataflow_urn = builder.make_data_flow_urn(
        orchestrator="spark", flow_id="social_warehouse", cluster="prod"
    )

    dataflow_info = DataFlowInfoClass(name="Social Warehouse", description="Social Warehouse for the Social Network Airflow Job")

    dataflow_info_mcp = MetadataChangeProposalWrapper(
        entityUrn=dataflow_urn,
        aspect=dataflow_info,
    )

    # Create an emitter to the GMS REST API.
    emitter = DatahubRestEmitter("http://localhost:8080")

    # Emit metadata!
    emitter.emit_mcp(dataflow_info_mcp)


    # Construct the DataJobInputOutput aspect for advertisements_users_views_clicks.
    input_datasets: List[str] = [
        builder.make_dataset_urn(platform="hive", name="social_db.advertisements", env="PROD"),
        builder.make_dataset_urn(platform="hive", name="social_db.users", env="PROD"),
        builder.make_dataset_urn(platform="hive", name="social_db.page_views", env="PROD"),
        builder.make_dataset_urn(platform="hive", name="social_db.clicks", env="PROD"),
    ]

    output_datasets: List[str] = [
        builder.make_dataset_urn(
            platform="hive", name="social_db.advertisements_users_views_clicks", env="PROD"
        )
    ]

    input_data_jobs: List[str] = [
        builder.make_data_job_urn(
            orchestrator="spark", flow_id="social_warehouse", job_id="advertisements_users_views_clicks", cluster="PROD"
        )
    ]

    datajob_input_output = DataJobInputOutputClass(
        inputDatasets=input_datasets,
        outputDatasets=output_datasets,
        inputDatajobs=input_data_jobs,
    )

    # Construct a MetadataChangeProposalWrapper object.
    # NOTE: This will overwrite all of the existing lineage information associated with this job.
    datajob_input_output_mcp = MetadataChangeProposalWrapper(
        entityUrn=builder.make_data_job_urn(
            orchestrator="spark", flow_id="social_warehouse", job_id="advertisements_users_views_clicks", cluster="PROD"
        ),
        aspect=datajob_input_output,
    )

    # Create an emitter to the GMS REST API.
    emitter = DatahubRestEmitter("http://localhost:8080")

    # Emit metadata!
    emitter.emit_mcp(datajob_input_output_mcp)

#add databricks tables, tableau, and EMR

if __name__ == "__main__":
    createBronzeTables()
    createSilverTables()
    createJobs()