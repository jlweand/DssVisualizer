package datacreator;

public class Screenshot {

	private String content;
	private String type;
	private String classname;
	private String title;
	private String comment;
	private String start;

	public Screenshot(){
	}
	public Screenshot(String content, String type, String classname, String title, String comment, String start){
		this.content = content;
		this.type = type;
		this.classname = classname;
		this.title = title;
		this.comment = comment;
		this.start = start;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getClassname() {
		return classname;
	}

	public void setClassname(String classname) {
		this.classname = classname;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}

	public String getStart() {
		return start;
	}

	public void setStart(String start) {
		this.start = start;
	}

}

