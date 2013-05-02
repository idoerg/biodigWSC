/**
 * 
 */
package org.biodig.tags;

import java.net.URI;
import java.util.Arrays;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.core.UriBuilder;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonReader;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import com.sun.jersey.api.client.config.ClientConfig;
import com.sun.jersey.api.client.config.DefaultClientConfig;
import com.sun.jersey.api.client.filter.HTTPBasicAuthFilter;
import com.sun.jersey.core.util.MultivaluedMapImpl;



public class TagAPI {
	private JsonParser jsonParser = null;
	private JsonArray MyDIGarray = null;
	private String URL;
	private String mediatype = "MediaType.APPLICATION_JSON";
	private ClientConfig config = null;
	private Client client = null;
	private WebResource service = null;
	private String requestpath;
	
	public TagAPI ( String URL ) {
		this.URL = URL;
		this.config = new DefaultClientConfig();
		this.client = Client.create(config);
		this.service = client.resource(getBaseURI());
	}
	
	//Convert string to URL to use with WebResource
	public URI getBaseURI() {
		return UriBuilder.fromUri(URL).build();
	}
	
	/*
	 * tags Methods
	 */
	
	//Get request for TAG Api
	public Tags getTAG (int id){		
		requestpath = "tags";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("id",Integer.toString(id));
		
		String info = (service.path(requestpath).queryParams(params).accept(mediatype).get(String.class));
		//System.out.println(info.toString());
		
		Gson myGson = new Gson();
		JsonParser jsonParser = new JsonParser();
		JsonElement tagSelement= jsonParser.parse(info);
		Tags newTag = myGson.fromJson(tagSelement, Tags.class);
		return newTag;
	}
	
	//Insert for TAG API
	public void insertTAG (TagQuery query) {
		requestpath = "tags";
			
			ClientResponse response = service.path(requestpath).accept(mediatype).post(ClientResponse.class,query.getQuery());
			System.out.println(response.toString());
		}
	
	//Edit Request for TAG API
	public void editTAG (int tagID, TagQuery query) {
		requestpath = "tags";
			query.addId(tagID);
			
			ClientResponse response = service.path(requestpath).accept(mediatype).put(ClientResponse.class,query.getQuery());
			System.out.println(response.toString());
		}
	
	//Delete request for TAG API
	public void deleteTAG(int id) {
		requestpath = "tags";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("id", Integer.toString(id));
		ClientResponse response = service.path(requestpath).queryParams(params).delete(ClientResponse.class);
		System.out.println(response.toString());
	}
	
	/*
	 * geneLinks Methods
	 */
	
	//Get request for TAG Api
	public geneLinks getGLinks (int id){		
		requestpath = "geneLinks";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("id",Integer.toString(id));
		
		String info = (service.path(requestpath).queryParams(params).accept(mediatype).get(String.class));
		//System.out.println(info.toString());
		
		Gson myGson = new Gson();
		JsonParser jsonParser = new JsonParser();
		JsonElement tagSelement= jsonParser.parse(info);
		geneLinks newGene = myGson.fromJson(tagSelement, geneLinks.class);
		return newGene;
	}
	
	//Insert for TAG API
	public void insertGLinks (TagQuery query) {
		requestpath = "geneLinks";
			
			ClientResponse response = service.path(requestpath).accept(mediatype).post(ClientResponse.class,query.getQuery());
			System.out.println(response.toString());
		}
	
	//Delete request for TAG API
	public void deleteGLinks(int geneId) {
		requestpath = "geneLinks";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("id", Integer.toString(geneId));
		ClientResponse response = service.path(requestpath).queryParams(params).delete(ClientResponse.class);
		System.out.println(response.toString());
	}
	
	

}
