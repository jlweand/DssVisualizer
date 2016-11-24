package datacreator;

public class ManualScreenshot extends Screenshot {

	private int manualscreen_id;

	public ManualScreenshot() {
	}

	public ManualScreenshot(int manualscreen_id, String content, String type, String classname, String title, String comment, String start) {
		super(content, type, classname, title, comment, start);
		this.manualscreen_id = manualscreen_id;
	}

	public int getManualscreen_id() {
		return manualscreen_id;
	}

	public void setManualscreen_id(int manualscreen_id) {
		this.manualscreen_id = manualscreen_id;
	}

}
