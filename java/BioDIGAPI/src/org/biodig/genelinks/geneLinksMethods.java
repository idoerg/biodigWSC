package geneLinks;

import images.imageData;
import images.imageDataQuery;

import java.net.URI;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.core.UriBuilder;
import javax.xml.ws.http.HTTPException;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.UniformInterfaceException;
import com.sun.jersey.api.client.WebResource;
import com.sun.jersey.api.client.config.ClientConfig;
import com.sun.jersey.api.client.config.DefaultClientConfig;
import com.sun.jersey.core.util.MultivaluedMapImpl;
import com.sun.jersey.multipart.FormDataMultiPart;

public class geneLinksMethods 
{

	//Local Variables used in the methods.
		private JsonParser jsonParser = null;
		private JsonArray MyDIGArray = null;
		private String URL;
		private String mediaType = "MediaType.APPLICATION_JSON";
		private ClientConfig config = null;
		private Client client = null;
		private WebResource service = null;
		private String requestpath;
		
		//Constructor that creates the information needed for API calls.
		public geneLinksMethods ( String URL ) {
			this.URL = URL;
			this.config = new DefaultClientConfig();
			this.client = Client.create(config);
			this.service = client.resource(getBaseURI());
		}
		
		//Converts a string to a URL compatable with WebResource.
		public URI getBaseURI() 
		{
			return UriBuilder.fromUri(URL).build();
		}
	
		/*
		Retrieves the GeneLink data from the BioDIG server using a unique Id that has been assigned during the POST
		Operation.
		*/
	public geneLinkData getGeneLinkInfo(int id) 
	{
		requestpath = "Genelinks";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("id",Integer.toString(id));

		String info = (service.path(requestpath).queryParams(params).accept(mediaType).get(String.class));
		System.out.println(info.toString());

		Gson myGson = new Gson();
		jsonParser = new JsonParser();
		JsonElement tagSelement= jsonParser.parse(info);
		geneLinkData newGeneLinkData = myGson.fromJson(tagSelement, geneLinkData.class);
		return newGeneLinkData;
	}
	
	//POST Operation that requires a TagID and optional parameters of name, organismId, and unique Name.
	 public void addGeneLink(int id, geneLinkQuery query)
	{
		requestpath = "Genelinks";
		query.addTagId(id);
			
			ClientResponse response = service.path(requestpath).accept(mediaType).post(ClientResponse.class,query.getQuery());
			System.out.println(response.toString());
	}
}
