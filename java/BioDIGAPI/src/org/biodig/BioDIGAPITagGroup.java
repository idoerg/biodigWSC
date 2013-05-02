package BioDIGAPI;

import java.net.URI;
import java.util.Arrays;
import java.util.Date;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.core.UriBuilder;

import org.json.JSONObject;
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

public class BioDIGAPITagGroup {
	private JsonParser jsonParser = null;
	private JsonArray MyDIGarray = null;
	private String URL;
	private String mediatype = "MediaType.APPLICATION_JSON";
	private ClientConfig config = null;
	private Client client = null;
	private WebResource service = null;
	private String requestpath;

	public BioDIGAPITagGroup ( String URL ) {
		this.URL = URL;
		this.config = new DefaultClientConfig();
		this.client = Client.create(config);
		this.service = client.resource(getBaseURI());
	}

	//Convert string to URL to use with WebResource
	public URI getBaseURI() {
		return UriBuilder.fromUri(URL).build();
	}

	//Get request for TagGroup API
	public TagGroup getTagGroup (int ID){	
		requestpath = "TagGroup";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("ID",Integer.toString(ID));

		String info = (service.path(requestpath).queryParams(params).accept(mediatype).get(String.class));
		System.out.println(info.toString());

		Gson myGson = new Gson();
		JsonParser jsonParser = new JsonParser();
		JsonElement tagSelement= jsonParser.parse(info);
		TagGroup newTagGroup = myGson.fromJson(tagSelement, TagGroup.class);
		return newTagGroup;
	}

	//Insert for TagGroup API
	public void postTagGroup (TagGroupQuery query) {
		requestpath = "TagGroup";

		ClientResponse response = service.path(requestpath).accept(mediatype).post(ClientResponse.class,query.getQuery());
		System.out.println(response.toString());
	}

	// Edit Request for TagGroup API
	public void putTagGroup (int ID, TagGroupQuery query) {
		requestpath = "TagGroup";
		query.addID(ID);

		ClientResponse response = service.path(requestpath).accept(mediatype).put(ClientResponse.class,query.getQuery());
		System.out.println(response.toString());
	}

	//Delete request for TagGroup API
	public void deleteTagGroup(int ID) {
		requestpath = "TagGroup";
		MultivaluedMap params = new MultivaluedMapImpl();
		params.add("ID", Integer.toString(ID));
		ClientResponse response = service.path(requestpath).queryParams(params).delete(ClientResponse.class);
		System.out.println(response.toString());
	}
}